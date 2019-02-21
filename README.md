# spack-repo

Spack repository for various packages not yet merged to mainline. Born for personal use whilst trying to get Flutter dependencies into mainline Spack.

### Usage

Usage is pretty easy, because Spack allows arbitrary repos (in priority order). Running the
following should attach this repository to your Spack setup:

```shell
$ git clone git@github.com:whitfin/spack-repo.git
$ spack repo add <PATH_TO_CLONE>
```

This will then make any of the specs in this repository available to install.
