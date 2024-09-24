FROM public.ecr.aws/docker/library/python:3.11-slim-buster

ARG PASSWORD

RUN apt-get update
RUN apt-get install -y openssh-server curl nano cron

RUN echo root:${PASSWORD} | chpasswd
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start
RUN useradd --user-group --system --create-home --no-log-init --shell /bin/bash ctf

WORKDIR /home/ctf/app

COPY requirements.txt .
RUN pip install -r ./requirements.txt && rm ./requirements.txt

COPY src/ .
RUN mkdir report
RUN chown -R ctf:ctf /home/ctf/app/report
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Add the cron job
RUN echo "*/5 * * * * find /home/ctf/app/report -type f -mmin +5 -exec rm -f {} \;" > /etc/cron.d/clean_report

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/clean_report

# Apply the cron job
RUN crontab /etc/cron.d/clean_report

ENTRYPOINT [ "./entrypoint.sh" ]