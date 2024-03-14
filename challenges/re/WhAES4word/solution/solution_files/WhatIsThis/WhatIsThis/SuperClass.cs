using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WhatIsThis
{
    abstract class SuperClass
    {
        private string nomeaning =
            "NvD&|v)7~o{}oT}}CmlT^,y1B(*|wom-mGO<K|$3v4Fs=)k$&T+A>}66_2%wg5%sX'fWe>s;&?AdU]nL9lIyKF(}0Vb_cg~wN:}qbHc6uAN{3qTaj+_`'+rpj}P#aHAMWSL$q5:C0I4LAg5[PCevE>WIN&PrpcK!^ng&'Aref&Fh_2Un+L9aS/#9T[C<J`-ts%Y{Fo8|><b#gh]p22KL|LdfhA4K,RG?N!3h%G8kG!T-6~oV/*mLC6sd_+!D&9f{J|s@6Dr=[pNz'TpcHlX>W3E%Tx=CPCOF6+HCI[xyx8fVfk%fDo]&:&-F:5XOqATG7}NMq,%dfyY#4o]bS`+wiC?P|g+y?Ij|IO(s'4wXqdzrSj|ho:k0De;q`(f&Ip][|-(?.mWiPd{q8CP;eyBTtA%(N6T?x8bc!S+jR[e:hkl%pn1SAJEfH/rpE'WV/-`;(>eaA:wJT3x1k#*De)!J:_fCm2xY=|WAcL-i39W)F&oNLi*yX/8za?7jCgFP!^x9H}|y0E&fSf`##./P$9W$@>4'eS/Mt{[;&Dp-lS>'LA}cm^%7pANe`m#%ryC'G/lI=sD%)zbGyLCqhi2.odY0['7hfsA?BBduv!rx--u@[o52&T$dp;#ET1SXL0[jzCSLPN~HMxouHS{,Si3-c@c@h[eH9nnm,~3qN;>n7$K}e/,@A-_LTSqe7<gbS,[%Pw9&!GEl{X,e],W>@z<>l7|L$ooozKhAF:NvU]gUq^P*!du;z&B.,)E_L0,0uK1mX9?vHS+a;#hS)+T57W+b]`S2hAH68kg-ujmX:2qWAX0jLNdwS0p'C9@#yON?x;y.i+BeX*$WK|>}/A&e9wD=D|}UVX]bWb_5b~!/A0tq*ox/MqO;9m?r*Bcrox%vV7nz{<5cMrmNTp@`BB?{_G#.,E&-JV@2;H86w-wz,y|jtaD/n,?f])Sab*(1vB(kF`i:`XAJc%+:i&AW]10a%T)ye!B)md~7O_=Kk{x+>&?EqSy";

        private List<byte> eyevee = new List<byte> { 0x54, 0x68, 0x69, 0x73, 0x49, 0x73, 0x41, 0x4C, 0x65, 0x65, 0x74, 0x49, 0x56, 0x40, 0x21, 0x23 }; 
        private int whatisnum = 12864;
        public double doubl = 2428;
        private List<SuperClass> WhatList = new List<SuperClass>();

        public SuperClass()
        {
            WhatList.Add(this);
        }

        public abstract int Funct1();
        public abstract SuperClass Whatisthis();
        public abstract string Part1OfFlag(int yy);

        public int Forreimp(List<int> v)
        {
            int x = v.Count;
            int y = 0;
            int z = 0;
            while (true)
            {
                int lol = whatisnum;
                z += v[y];
                y++;
                if (y == x)
                {
                    break;
                    whatisnum++;
                }
            }
            return z;
        }
        public int forl(List<int> v)
        {
            int z = 0;
            foreach (int i in v)
            {
                z += i;
            }

            return z;
        }
        public string Forreimp(List<char> v)
        {
            int x = v.Count;
            int y = 0;
            string z = "";
            while (true)
            {
                z += v[y];
                y++;
                if (y == x)
                {
                    break;
                }

                char reei = nomeaning[1];
            }
            return z;
        }

        public int Return0(string h)
        {
            List<int> intlist = new List<int>
            {
                1, 2, 3, 4, 5, 6, 2, 4, 1, 7, 10, 7, 12, 12, 15, 3, 11, 18, 14, 12, 18, 17, 21, 5, 6, 24, 2, 21, 16, 8,
                10, 15, 2, 1, 22, 36, 17, 12, 13, 37, 19, 3, 38, 35, 26, 28, 4, 20, 47, 26, 37, 44, 19, 48, 46, 3, 56,
                24, 10, 40, 11, 34, 52, 55, 15, 10, 31, 58, 22, 62, 55, 64, 63, 36, 3, 28, 49, 17, 52, 9, 63, 27, 52,
                66, 50, 58, 53, 45, 24, 21, 42, 71, 57, 84, 87, 77, 10, 28, 84
            };
            int a = Forreimp(intlist);
            List<char> clist = new List<char>{ '(', 'd', '@', 'O', 'i', 'V', 'v', 'N', 'e', 'K', 'q', 'J', '8', 'J', '_' ,'T' ,'.' ,'U' ,'A' ,'G' ,']' ,'1' ,'Y' ,'1' ,'@' ,'U' ,'R' ,'#' ,'0' ,'v' ,'*' ,'l' ,'S' ,'&' ,'W' ,'b' ,'7' ,'K' ,'&' ,'K' ,'C' ,'I' ,'R' ,'&' ,'S' ,'+' ,'7' ,'q' ,'O' ,'v' ,'3' ,'G' ,'d' ,'<' ,'*' ,'S' ,'H' ,'t' ,'o' ,'U' ,'$' ,'&' ,'i' ,'h' ,'8' ,'Y' ,'w' ,'h' ,'j' ,'F' ,'_' ,'j' ,'$' ,'-' ,'p' ,'U' ,'7' ,'I' ,':' ,'.' ,'A' ,'T' ,'%' ,'$' ,'L' ,'-' ,'X' ,'<' ,'O' ,'`' ,'E' ,'<' ,'F' ,'1' ,'@' ,'K' ,'3' ,'^' ,'~' ,'b' ,';' ,'}' ,'[' ,'`' ,'4' ,'g' ,'x' ,'2' ,'&' ,'u' ,'<' ,'f' ,'@' ,'n' ,'F' ,'W' ,']' ,'D' ,'C' ,':' ,'#' ,'`' ,'V' ,'Y' ,'e' ,'y' ,'~' ,'g' ,'=' ,')' ,'e' ,'(' ,'!' ,'c' ,'m' ,'R' ,'d' ,'r' ,'d' ,'M' ,'0' ,']' ,'&' ,'%' ,'}' ,'}' ,':' ,'4' ,'B' ,'%' ,'S' ,'0' ,';' ,'H' ,'@' ,'x' ,'#' ,'8' ,'D' ,'V' ,'~' ,'X' ,'{' ,'_' ,'P' ,'6' ,'/' ,'V' ,'x' ,'6' ,'2' ,'X' ,'v' ,'j' ,'a' ,'v' ,'t' ,'%' ,'w' ,'(' ,'w' ,'1' ,'C' ,'r' ,'U' ,'x' ,')' ,'7' ,'/' ,'p' ,'u' ,'b' ,'/' ,'A' ,'M' ,'.' ,'p' ,'T' ,'[' ,'Y' ,'v' ,')' ,'m' ,')' ,'H' ,'h' ,',' ,'1' ,'g' ,'a' ,'a' ,'[' ,'[' ,'j' ,'L' ,'G' ,'x' ,'[' ,'w' ,'A' ,'$' ,'S' ,'&' ,'!' ,'(' ,'_' ,'y' ,'^' ,'(' ,'*' ,'T' ,'#' ,'[' ,'R' ,'#' ,')' ,'q' ,'i' ,'e' ,'K' ,'B' ,'b' ,'(' ,'r' ,'T' ,'O' ,'n' ,'q' ,'%' ,'s' ,'M' ,':' ,'v' ,'r' ,'D' ,'b' ,'U' ,'B' ,'i' ,':' ,'<' ,'D' ,'F' ,'S' ,'*' ,'s' ,'i' ,'S' ,'<' ,'$' ,'1' ,'H' ,'k' ,'n' ,';' ,'3' ,'?' ,'>' ,'>' ,'(' ,'u' ,'T' ,'G' ,'S' ,'C' ,'C' ,'-' ,'x' ,'E' ,'*' ,'}' ,'<' ,'!' ,'{' ,'~' ,'E' ,'n' ,'O' ,'|' ,'U' ,'y' ,'n' ,'n' ,'/' ,'3' ,'D' ,'C' ,'R' ,'O' ,'8' ,'q' ,'^' ,'w' ,'~' ,'X' ,'H' ,'z' ,'0' ,'7' ,'0' ,'m' ,'$' ,'L' ,'s' ,'$' ,'g' ,'[' ,'Y' ,',' ,'A' ,'u' ,'_' ,'t' ,'Y' ,'q' ,'@' ,'J' ,'=' ,'%' ,'B' ,'o' ,'>' ,'>' ,'H' ,'?' ,'@' ,'V' ,'V' ,';' ,'r' ,'=' ,'R' ,'t' ,'<' ,'W' ,'b' ,'Y' ,'k' ,'U' ,'O' ,'&' ,'s' ,'y' ,'W' ,'1'  ,'h' ,'x' ,'d' ,'P' ,'2' ,'<' ,'X' ,'Y' ,'X' ,'I' ,'['  ,'`' ,'*' ,'2' ,'y' ,'2' ,'T' ,'D' ,'w' ,'E' ,'+' ,'$' ,'s' ,'?' ,':' ,'D' ,'e' ,'P' ,'d' ,'P' ,'*' ,'!' ,'E' ,'5' ,'C' ,'x' ,'#' ,',' ,'6' ,'&' ,'f' ,')' ,'V'  ,'M' ,'%' ,'&' ,'F' ,'k' ,'?' ,'F' ,'K' ,'~' ,'7' ,'s' ,'|' ,'a' ,'2' ,'U' ,'X' ,')' ,'i' ,']' ,'T' ,'.' ,'[' ,'w' ,'Y' ,'G' ,'M' ,'z' ,'_' ,'x' ,'<' ,'~' ,';' ,'j' ,'v' ,'w' ,'^' ,'K' ,'d' ,'2' ,'F' ,'2' ,'w' ,'7' ,'}' ,'<' ,'e' ,'^' ,'4' ,'H' ,'U' ,'E' ,')' ,'M' ,'`' ,'h' ,'M' ,'`' ,'P' ,'h' ,'a' ,'f' ,'y' ,'W' ,'z' ,'z' ,'I' ,'<' ,'u'  ,'B' ,'{' ,'_' ,'[' ,'&' ,'L' ,'p' ,'J' ,'k' ,'&' ,'p' ,'Y' ,'?' ,'5' ,'a' ,'J' ,'V'  ,'p' ,'w' ,'t' ,'q' ,'i' ,'_' ,'T' ,'~' ,'8' ,'A' ,'`' ,'.' ,'K' ,'+' ,'q' ,'&' ,'1' ,'U' ,'i' ,'y' ,'f' ,'g' ,'q' ,'p' ,'U' ,'!' ,'!' ,'b' ,':' ,'3' ,':' ,'E' ,'S' ,'a' ,'M' ,'?' ,'G' ,'{' ,'8' ,'o' ,'?' ,'U' ,'1' ,'~' ,'t' ,'d' ,'y' ,'L' ,'C' ,'*' ,'b' ,'-' ,'n' ,'}' ,'M' ,'O' ,'q' ,'w' ,'L' ,'S' ,'B' ,'O' ,'G'  ,',' ,'~' ,'b' ,'G' ,'<' ,'J' ,'U' ,'*' ,'U' ,'R' ,'N' ,'=' ,'K' ,'v' ,'o'  ,'(' ,'L' ,'N' ,'8' ,'q' ,'t' ,'q' ,'6' ,'O' ,'U' ,'(' ,'g' ,'$' ,'}' ,'X' ,'[' ,';' ,'m' ,'P' ,'d' ,'S' ,'I' ,'k' ,'(' ,'.' ,'c' ,'A' ,'T' ,'A' ,'~' ,'~' ,'0' ,'8' ,'z' ,'N' ,'k' ,'E' ,'P' ,'_' ,'f' ,']' ,'V' ,'P' ,'9' ,'~' ,'M' ,'^' ,',' ,'b' ,'[' ,'A' ,'O' ,'D' ,'V' ,'s' ,'}' ,'N' ,'q' ,'z' ,',' ,'e' ,'<' ,'K' ,')' ,'&' ,'u' ,'i' ,'8' ,'v' ,'0' ,'E' ,'t' ,'s' ,'^' ,'e' ,'f' ,'|' ,'/' ,'|' ,'h' ,'O' ,'P' ,'s' ,'$' ,'n' ,'p' ,'k' ,'v' ,'A' ,'l' ,'q' ,'9' ,'[' ,'i' ,'r' ,'}' ,'t' ,'1' ,'W' ,'}' ,'I' ,'W' ,'^' ,':' ,'M' ,'(' ,'P' ,'3' ,'I' ,'W' ,'S' ,'P' ,'S' ,':' ,'=' ,'~' ,'|' ,'a' ,'`' ,'l' ,'P' ,'w' ,'I'  ,',' ,'J' ,'3' ,'L' ,'I' ,':' ,'F' ,'N' ,'H' ,'[' ,'k' ,']' ,'=' ,'m' ,'|' ,'9' ,'$' ,'%' ,'K' ,'`' ,'T' ,';' ,';' ,'4' ,'3' ,'c' ,'1' ,'E' ,'4' ,'y' ,'f' ,'{' ,',' ,'n' ,'Y' ,'!' ,'5' ,'S' ,'i' ,'p' ,'b' ,'S' ,'J' ,'0' ,'_' ,'d' ,'w' ,'R' ,'-' ,'B' ,'Y' ,'G' ,'G' ,'X' ,'n' ,'V' ,'Y' ,'6' ,'j' ,')' ,'D' ,'r' ,'+' ,'J' ,'a' ,'C' ,'6' ,'i' ,',' ,')' ,'C' ,'9' ,'g' ,'I' ,'|' ,'v' ,'v' ,'/' ,'o' ,'/' ,'(' ,',' ,'q' ,'q' ,'r' ,';' ,'w' ,'I' ,'`' ,'9' ,'n' ,'C' ,'d' ,'#' ,')' ,'b' ,'k' ,'9' ,']' ,'.' ,'t' ,'H' ,'4' ,'i' ,'J' ,'J' ,'A' ,'o' ,'*' ,'T' ,'M' ,'o' ,';' ,'j' ,'_' ,'M' ,'q' ,'$' ,'}' ,'p' ,'F' ,'%' ,'i' ,'X' ,'c' ,'?' ,'A' ,'[' ,'|' ,'m' ,'~' ,'3' ,'4' ,'1' ,'c' ,'s' ,'e' ,'}' ,'P' ,'d' ,'<' ,'p' ,'k' ,'O' ,'{' ,'%' ,'}' ,'S' ,'W' ,'E' ,'>' ,'l' ,'8' ,'!' ,'k' ,'3' ,'i' ,'2' ,'k' ,'I' ,'c' ,'v' ,'P' ,'q' ,'B' ,'T' ,'^' ,'R' ,'N'  ,'N' ,'v' ,'P' ,'(' ,'`' ,',' ,'V' ,'3' ,'C' ,']' ,'W' ,'D' ,'.' ,'*' ,'E'  ,'G' ,'_' ,'t' ,'@' ,'f' ,'B' ,'8' ,'C' ,'v' ,'i' ,'b' ,'(' ,'h' ,'0' ,'_' ,'n' ,'!' ,'/' ,'~' ,'w' ,'P' ,'v' ,'q' ,'s' ,'i' ,',' ,'y' ,'a' ,'E' ,'q' ,'C' ,'3' ,'P' ,'i' ,'N' ,'g' ,')' ,'}' ,'&' ,'^' ,'4' ,'r' ,'n' ,'k' ,'0' ,'f' ,'v' ,'J' ,'=' ,'q' ,'.' ,'1' ,'x' ,'R' ,'r' ,'4' ,'Y' ,')' ,'j' ,'R' ,'<' ,'1' ,'J' ,'X' ,'#' ,'O' ,'y' ,'8' ,'O' ,'D' ,'W' ,'h' ,'F' ,'P' ,'y' ,'$' ,'$' ,'A' ,'T' ,'K' ,'|' ,'V' ,'9' ,'L' ,'B' ,'O' ,'F' ,'r' ,'=' ,'z' ,'i' ,'.' ,'c' ,'`' ,'n' ,'i' ,':' ,'9' ,'?' ,'s' ,'r' ,'L' ,'h' ,'+'};
            string f = "";
            f = Forreimp(clist);
            double r = f.Length + a;
            double dd = Math.Pow(r, 99);
            double x = dd / 2;
            return Convert.ToInt32(0 / x);
        }

        public int ett()
        {
            // Declare and initialize variables
            int num1 = 10;
            int num2 = 20;
            int sum = 0;

            // Calculate the sum of num1 and num2
            if (num1 > num2)
            {
                sum = num1 + num2;
            }
            else if (num2 > num1)
            {
                sum = num2 + num1;
            }
            else
            {
                sum = num1 * num2;
            }

            // Print the sum to the console
            Console.WriteLine("The sum is: " + sum);

            // Check if the sum is even or odd
            if (sum % 2 == 0)
            {
                Console.WriteLine("The sum is even.");
            }
            else
            {
                Console.WriteLine("The sum is odd.");
            }

            return 8000;
        }

        public string snd()
        {
            if (80000 == ett())
            {
                return snd();
            }
            else
            {
                if (8000 == ett())
                {
                    SuperClass s = new SubClass();
                    s.ett();
                    Convert.ToString(s);
                    return "8ac7";
                }

                return "";
            }
        }

        public string Str()
        {
            return "ca";
        }
        public int FakeFirstLetterofFlag()
        {
            bool iii = false;
            long ii = 0;
            List<int> ISwearToGod = new List<int> { 1, 1, 1, 2, 3, 3, 3, 4, 2, 2, 4, 2, 4, 2, 242, 2, 2, 2 };
            foreach (int i in ISwearToGod)
            {
                Console.WriteLine(i);
                ii += i;
            }

            if (ii > 99)
            {
                iii = true;
            }

            if (iii)
            {
                ii = 11;
            }
            return Convert.ToInt32(ii * 0);
        }

        public string MemeBigBoi()
        {
            int number = 10;
            bool expr = false;
            while (!expr)
            {
                for (int i = 1; i <= 10; i++)
                {
                    if (i != 0)
                    {
                        expr = true;
                        break;
                    }

                    if (number % i == 0)
                    {
                        if (i == 1 || i == number)
                        {
                            Console.WriteLine("The number " + number + " is a prime number.");
                        }
                        else if (expr)
                        {
                            return "qwefggdf";
                            break;
                        }
                        else
                        {
                            Console.WriteLine("The number " + number + " is not a prime number.");
                            break;
                        }
                    }
                }
            }
            if (expr)
            {
                return "0fa9f9410";
            }
            else
            {
                return "";
            }
        }

        public string SupDudes()
        {
            double sup2 = 0;
            List<int> Sup = new List<int>{1,1,1,1,1,1,1,1,1,1,1};
            foreach (int sup in Sup)
            {
                sup2 = Math.Pow(sup, 2);
            }
            string sups = Convert.ToString(sup2);
            string whysup = "64";
            return whysup;
            return sups;
            return "";
            return "This is my fight song dudes.";
            return "My Life";
            return "I love C# .NET so much.";
        }

        public string IDK()
        {
            char kjdk;
            double a = 0;
            string iii = "kkjsjfqwefgxc vsdsjfjdkjfkjdksjkd";
            foreach (char csss in iii)
            {
                kjdk = csss;
                a++;
            }

            for (uint x = 0; x < 123; x++)
            {
                if (x == 0)
                {
                    Console.WriteLine();
                }
                else if (x == 1)
                {
                    Console.WriteLine(",");
                }
                else if (x == 100)
                {
                    return "25";
                }
            }

            return "";
        }

        public string finalcheck()
        {
            int y = 0;
            string a = "3af";
            string b = "e8f";
            for (int x = 0; x < 40; x++)
            {
                Console.WriteLine(a + b + Convert.ToString(x));
                y++;
            }

            return a + b + Convert.ToString(y);
        }
    }
}
