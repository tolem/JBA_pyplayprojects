#!/usr/bin/env bash
RANDOM=4096
responses=( "Perfect!" "Awesome!" "You are a genius!" "Wow!" "Wonderful!" )
score=10
count=0
file_name=scores.txt
echo -e "Welcome to the True or False Game!\n"
  user_data=$(curl -s http://0.0.0.0:8000/download/file.txt)
  user=$( echo "$user_data" | sed 's/.*"username": *"\{0,1\}\([^,"]*\)"\{0,1\}.*/\1/')
  password=$( echo "$user_data" | sed 's/.*"password": *"\{0,1\}\([^,"]*\)"\{0,1\}.*/\1/')
  curl http://0.0.0.0:8000/login -u "${user,,}:$password" -sc cookie.txt &>/dev/null

menu() {
    echo "0. Exit"
    echo "1. Play a game"
    echo "2. Display scores"
    echo "3. Reset scores"
    echo "Enter an option:"
    read -r option && count=0
}

play() {
  while true;
  do
    response=$( curl http://0.0.0.0:8000/game -sb cookie.txt)
    question=$( echo "$response" | sed 's/.*"question": *"\{0,1\}\([^,"]*\)"\{0,1\}.*/\1/')
    answer=$( echo "$response" | sed 's/.*"answer": *"\{0,1\}\([^,"]*\)"\{0,1\}.*/\1/')
    echo "$question"
    echo "True or False?" && read -r answer_user
      if [ "$answer" == "$answer_user" ]; then
        ((count++))
        indx=$((RANDOM%5))
        echo "${responses[$indx]}"
      else
        echo "Wrong answer, sorry!"
        echo "$name you have $count correct answer(s)."
        echo "Your score is $(( "$count" * "$score" )) points."
        echo "User: $name, Score: $(( "$count" * "$score" )), Date: $(date +"%Y-%m-%d")" >> $file_name
        break;
      fi
  done
}

while true;
do
  menu
  case $option in
      0 | 'quit')
          echo "See you later!"
          break;
          ;;
      1)
        echo "What is your name?" && read -r name
        play;;
      2)
        if [ -e "$file_name" ]; then
          echo "Player scores"
          cat "$file_name"
        else
          echo "File not found or no scores in it!"
        fi
          ;;
      3)
        if [ -e "$file_name" ]; then
          rm $file_name && echo "File deleted successfully!"
          else
          echo "File not found or no scores in it!"
          fi
          ;;
      *)
        echo -e "Invalid option!\n";;
  esac
done
