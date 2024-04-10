# 2024
This repository is the official challenge repository for [Lag and Crash 4.0](https://lagncra.sh/).

## Scoreboard (Closed-Division)
The closed division contains teams with exactly five (5) members, each from either a secondary school, junior college, polytechnic, ITE or the equivalent.

![closed](https://i.gyazo.com/ccaec5a4f2819a5bbcd1b01376217bdd.png)
## Scoreboard (Open-Division)
The open division contains teams with any number of members, each from any educational institution; including non-students.

![open](https://i.gyazo.com/3c35a66dce1bab9d34b156d485a3556a.png)

## Navigation
Each challenge in the [challenges](./challenges/) directory is categorised by its respective category, with at least one of the following subdirectories:
- `service`: Contains the service files for the challenge, i.e `Dockerfile`, `docker-compose.yml`, etc.
- `solution`: Contains the solution files for the challenge, and a writeup usually called in `README.md` or `writeup.md`.
- `dist`: Contains the distribution files given to the participants, if any.

## Deployment
Hosted challenges can be deployed via the provided [docker-compose.yml](./docker-compose.yml) file, hosted challenges are split into three docker profiles: `wave1`, `wave2` and `wave3`.

Docker profiles (as far as I know) are only available in Docker Compose v2.0, which is currently in beta. To use Docker Compose v2.0, you can install it via the official documentation: [here](https://docs.docker.com/compose/)

### Deploying a Specific Challenge
To deploy a challenge, run the following command:
```sh
docker compose up -d [service_name]
```

### Deploying a Wave
To deploy a wave, run the following command:
```sh
docker compose up -d --profile wave[1/2/3]
```

### Deploying ALL Challenges
You can deploy multiple or all profiles at once by running the following command:
```sh
docker compose up -d --profile wave1 --profile wave2 --profile wave3
```

## Contributing
We're open to contributions, feel free to open a pull request or an issue if any of the challenges are broken; but challenge authors may or may not actively maintain their challenges.

This repository should be assumed to be in a "frozen" state, meaning that you shouldn't expect quick responses to issues or pull requests.
