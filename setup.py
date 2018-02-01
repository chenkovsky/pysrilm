from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os.path
import platform
import os
# Adjust to point to your SRILM build directory
SRILM_DIR = os.environ.get("SRILM") or "/opt/srilm"
# Adjust to match your architecture -- if unsure, build SRILM and then see
# what subdirectories you have in SRILM_DIR/lib/.
uname = platform.uname()
if uname.system == "Darwin":
    SRILM_ARCH = "macosx"
elif uname.machine == "x86_64":
    SRILM_ARCH = "i686-m64"
else:
    raise "Not supported Now"

SRILM_INCLUDE_DIR = os.path.join(SRILM_DIR, "include")
SRILM_LIB_DIR = os.path.join(SRILM_DIR, "lib", SRILM_ARCH)

setup(
    name="srilm",
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
      Extension("srilm",
                ["srilm.pyx"],
                language="c++",
                include_dirs=[SRILM_INCLUDE_DIR],
                libraries=["oolm", "dstruct", "misc"],
                extra_compile_args=['-fopenmp'],
                extra_link_args=["-L" + SRILM_LIB_DIR, '-lgomp', '-lz', '-liconv'],
                )
      ],
)
