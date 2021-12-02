git submodule add https://github.com/octopusengine/octopuslab.git
git submodule init
cd octopuslab/esp32-micropython && git submodule init && cd ../..
git submodule update --recursive

