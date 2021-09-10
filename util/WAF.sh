#!/bin/bash
sudo nvme smart-log /dev/nvme3n2 > SMART-Before.txt
sudo ../../../output/db_bench "$(< Config.txt)"
# ../../../output/zenfs_test --zbd=nvme3n2
sudo nvme smart-log /dev/nvme3n2 > SMART-After.txt
python WAF.py
