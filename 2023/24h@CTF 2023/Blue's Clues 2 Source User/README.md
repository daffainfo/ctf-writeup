# Welcome!
> Martin the devops engineer sends you a copy of what the weird CI/CD pipeline does:

```
variables:
  PRIVATE_KEY_GITLAB: |
    -----BEGIN OPENSSH PRIVATE KEY-----
    b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
    QyNTUxOQAAACAWFFrVpN4X2AduHjJhV7W5NEBxs0n2fwF3/+ig86EqTAAAAKAoGJ+vKBif
    rwAAAAtzc2gtZWQyNTUxOQAAACAWFFrVpN4X2AduHjJhV7W5NEBxs0n2fwF3/+ig86EqTA
    AAAECw7Qmm2do1DNITF0147jS8q99/Re2/9SV4iJlNN2GzKBYUWtWk3hfYB24eMmFXtbk0
    QHGzSfZ/AXf/6KDzoSpMAAAAHGJhY2t1cHNAUmV6aWZwLUdpdExhYi1TZXJ2ZXIB
    -----END OPENSSH PRIVATE KEY-----
  PRIVATE_KEY_FS: |
    -----BEGIN OPENSSH PRIVATE KEY-----
    b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
    QyNTUxOQAAACBqwJbg0jEAhyNKSt4i8FStwU8RA7wvvZbTqpCEhQUjtQAAAKAiB9rPIgfa
    zwAAAAtzc2gtZWQyNTUxOQAAACBqwJbg0jEAhyNKSt4i8FStwU8RA7wvvZbTqpCEhQUjtQ
    AAAEBVDBKygi9Cq1JJUuCPtXCVcPzVCmO0zWhVrPS9v43ZFWrAluDSMQCHI0pK3iLwVK3B
    TxEDvC+9ltOqkISFBSO1AAAAF0xpbnV4QWRtaW5ARmlsZVNlcnZlcjAyAQIDBAUG
    -----END OPENSSH PRIVATE KEY-----
  PRIVATE_KEY_WEB: |
    -----BEGIN OPENSSH PRIVATE KEY-----
    b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
    QyNTUxOQAAACBxALoFgiT34kOecbp7apS5zLKmVIWDtF9XJH0wTJIUywAAAKhGbRnhRm0Z
    4QAAAAtzc2gtZWQyNTUxOQAAACBxALoFgiT34kOecbp7apS5zLKmVIWDtF9XJH0wTJIUyw
    AAAEBwHzDMUnHlEuTOM0xAfoTAQzbBb2B2S3ubo5MqII/6SnEAugWCJPfiQ55xuntqlLnM
    sqZUhYO0X1ckfTBMkhTLAAAAIFJlemlmcEFkbWluQFJlemlmcC1HaXRMYWItU2VydmVyAQ
    IDBAU=
    -----END OPENSSH PRIVATE KEY-----

stages:
  - deploy

deploy-job:
  stage: deploy
  environment: production
  script:
    - chmod u+x ./health-agent
    - nohup ./health-agent &
    # - eval "$(ssh-agent -s)"
    # - echo "${PRIVATE_KEY_WEB}"
    # - echo -n "${PRIVATE_KEY_WEB}" | ssh-add -
    # - rsync -zPe "ssh -o StrictHostKeyChecking=no" ./ Webmestre@10.0.0.5:/tmp/
    # - ssh -Nf -o "StrictHostKeyChecking=no" Webmestre@10.0.0.5 'chmod u+x /tmp/health-agent; nohup ./health-agent &'
  tags:
    - shell
```

> This is clearly malicious. Before going further, we need to go back. How did this pipeline get there? Find the username that created the rogue CI/CD pipeline.

## About the Challenge
We need to find the username that created the malicious CI/CD pipeline

## How to Solve?
In the KQL syntax, I inputted `health-agent` because I want to see some logs that contains string `health-agent` and contain the username. I checked one of the logs and we found the username that created the malicious CI/CD pipeline

![flag](images/flag.png)

```
yvandescreds
```