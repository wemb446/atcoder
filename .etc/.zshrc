alias aci="_aci"
alias act="oj t -c 'python3 main.py' -d tests"
alias acs="acc submit main.py"

alias code="_code"

function _aci() {
  cd /Users/{usr_name}/dev/atcoder
  acc new $1
  python3 .init.py $1
}

  function _code() {
  if [[ $# = 0 ]]
  then
    open -a "Visual Studio Code"
  else
    local argPath="$1"
    [[ $1 = /* ]] && argPath="$1" || argPath="$PWD/${1#./}"
    open -a "Visual Studio Code" "$argPath"
  fi
}
