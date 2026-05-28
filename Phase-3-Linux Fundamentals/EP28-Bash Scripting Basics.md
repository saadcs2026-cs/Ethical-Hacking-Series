# EP 28 — Bash Scripting Basics

## What is Bash Scripting?
Bash is Linux's built in scripting language.
Write commands in a file and
run them all at once automatically!

## Creating a Script
touch script.sh      # create file
chmod +x script.sh   # make executable
./script.sh          # run script

## Basic Script Structure
#!/bin/bash
# This line tells Linux to use bash
# Lines starting with # are comments

echo "Hello from CodeShield!"

## Variables
#!/bin/bash
name="Saad"
age=18
echo "My name is $name"
echo "I am $age years old"

## User Input
#!/bin/bash
read -p "Enter your name: " name
echo "Welcome $name!"

## Conditions
#!/bin/bash
read -p "Enter password: " pass

if [ "$pass" == "1234" ]; then
    echo "Access Granted!"
else
    echo "Wrong Password!"
fi

## Loops
#!/bin/bash

# For loop
for i in {1..5}; do
    echo "Number: $i"
done

# While loop
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

## Practical Hacking Script
#!/bin/bash
# Simple port scanner
target=$1
for port in {1..100}; do
    (echo >/dev/tcp/$target/$port) 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Port $port is OPEN"
    fi
done

## Follow on Instagram
@code.shield_ for full episode!
