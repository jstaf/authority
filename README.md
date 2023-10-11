# authority

This is a `sudo` audit plugin that makes your computer play the "AUTHORITY" line
from Baldur's Gate 3 every time you run `sudo`. Now your family and coworkers
can know how much of a fucking nerd you are (they probably already know though).
It'll skip playing the sound if it's played in the last 5 minutes to prevent
things from getting too annoying.

I mostly wrote this as a joke. I don't recommend actually installing it on any
super critical systems. Because of it's very nature as a sudo plugin _it can
break sudo_ if installation somehow goes wrong or you make a syntax error
somewhere. Obviously, use at your own risk. There are no guarantees. It might
kill your cat.

## Installing

Because this is a sudo plugin, **_it has the potential to break sudo_** if
something goes wrong with the installation. You should open a root shell with
`sudo su -` BEFORE INSTALLATION and then CHECK THAT SUDO WORKS after
installation in a second terminal window (`sudo echo test`). This will let you
rollback the changes if you have somehow messed sudo up.

**Before installing, install `ffmpeg` via your package manager:**

- OpenSUSE - `sudo zypper install ffmpeg`
- Ubuntu/Debian - `sudo apt update && sudo apt install ffmpeg`
- Fedora -
  ```
  sudo dnf install \
    https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
    https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
  sudo dnf install ffmpeg
  ```

Once you've installed ffmpeg, install the plugin with:

```bash
sudo su -
make install

# in a second terminal, make sure sudo still works:
sudo echo "Authority."
# if that didn't work, immediately uninstall with "sudo make uninstall"
```

## Uninstall

You can completely purge the plugin from your system with:

```bash
sudo make uninstall
```

Alternatively, just comment out the `Plugin python_audit ...` line in
`/etc/sudo.conf` to temporarily turn off the plugin without completely
uninstalling it.
