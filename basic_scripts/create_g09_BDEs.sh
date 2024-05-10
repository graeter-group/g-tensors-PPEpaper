while getopts 'f:h' flag; do
  case "${flag}" in
    f) file=${OPTARG} ;;

    h) print_help ;;
    *) echo "for usage check: myutils <function> -h" >&2 ; exit 1 ;;
  esac
done

myutils change_distance opt.xyz g09BDE "" 0 0 "scale_distance"

sed -i "1a %NProcShared=8" g09BDE.com
sed -i "s/^0 1$/0 2/g" g09BDE.com
sed -i "s/%chk=test/%chk=g09BDE/g" g09BDE.com
sed -i "3a opt(modredun,calcfc) freq" g09BDE.com
