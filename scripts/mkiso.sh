VERSION=$1
if [ -z $VERSION ];then
    echo "no version input"
    exit 1
fi

NAME="centos7_v$VERSION"
echo $NAME > isolinux/version.txt
mkisofs -o dist/${NAME}.iso -b isolinux.bin -c boot.cat -no-emul-boot \
        -V 'CentOS7' \
        -boot-load-size 4 -boot-info-table -R -J -v -T isolinux
echo '************'
echo "path: dist/${NAME}.iso"
echo 'Done!'
