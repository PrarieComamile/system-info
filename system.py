import platform

# Architecture
architecture = (platform.architecture()[0])

# machine
machine = (platform.machine())

# node
node = (platform.node())

# system
system = (platform.system())

# platform
os_platform = (platform.platform(aliased=0, terse=0))

# os version
os_version = (platform.version())

# os name
os_name = (platform.freedesktop_os_release()["PRETTY_NAME"])

# os version local
os_version_local = (platform.freedesktop_os_release()["VERSION"])

# os base
os_base = (platform.freedesktop_os_release()["ID_LIKE"])

# os support
os_support = (platform.freedesktop_os_release()["SUPPORT_URL"])
