#!/bin/bash
sudo nvme smart-log /dev/nvme3n2 > before.txt
sudo ../../../output/zenfs_test --zbd=nvme3n2
sudo nvme smart-log /dev/nvme3n2 > after.txt
sudo WAF.py