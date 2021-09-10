#!/bin/bash

# format
rm -rf /tmp/zenfs_nvme3n2
sudo ../../../output/zenfs mkfs --aux_path=/tmp/zenfs_nvme3n2 --zbd=nvme3n2 --force

# before
sudo nvme smart-log /dev/nvme3n2 > SMART-Before.txt

# run test
sudo sh WAFTestConfig.sh
#sudo ../../../output/db_bench "$(< Config.txt)"
# ../../../output/zenfs_test --zbd=nvme3n2

# after
sudo nvme smart-log /dev/nvme3n2 > SMART-After.txt

# WAF calculation
python WAFCalculation.py