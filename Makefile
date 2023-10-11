.PHONY = install, uninstall

install:
	mkdir -p /usr/local/share/sudo-authority
	install -m 755 authority.py /usr/local/share/sudo-authority/
	install -m 644 authority.mp3 /usr/local/share/sudo-authority/
	echo "Plugin python_audit python_plugin.so ModulePath=/usr/local/share/sudo-authority/authority.py ClassName=Authority" >> /etc/sudo.conf 

uninstall:
	sed -i '/^Plugin python_audit/d' /etc/sudo.conf
	rm -rf /usr/local/share/sudo-authority
