## Description

This repo's result data is reported by 3 benchmarks:

| Name | Repo |
| ---- | ---- |
| Gas Benchmarks | https://github.com/OpenFusionist/gas-benchmarks/tree/rc-1 |
| Huge Genesis.json File Benchmarks | https://github.com/OpenFusionist/genesis-init-benchmarks |
| Burntpix Benchmarks | https://github.com/OpenFusionist/gas-benchmarks/tree/burnt-rc-1 |

## Update client version

The configuration file for the client version is [images.yaml](https://github.com/OpenFusionist/benchmarks-data-results/blob/main/images.yaml). All benchmark repositories will use this configuration file when the script is running. If you want to upgrade the client version, submit a pull request to update this file in this repository.

## Run benchmarks yourself

### 1. You need a Linux server

Install these packages on your server:

- Python 3.10
- Docker
- Docker Compose
- .NET 8.0.x
- `make` (for running make commands)

### 2. Fork this repo

Check this [GitHub Action Script](https://github.com/OpenFusionist/benchmarks-data-results/blob/main/.github/workflows/run_all.yml). After forking this repo, set up these Secrets in your repo:

- PRIVKEY
- REMOTE_IP

The `PRIVKEY` is the key that has authorization to access your server, and the `REMOTE_IP` is your server's IP address.

### 3. (Optional) Set up git commit info and push your results

You can set up this info on your server:

```
git config --global user.email "benchmarks@fsn.io"
git config --global user.name "Benchmarks Bot"
```

And set the secrets variable in your repo:

- GIT_TOKEN_PREFIX

The value should be like `username:ghp_****@`. This will allow your actions to submit your result report data after the run is finished.


