#!/usr/bin/python3
# Author: Martin Basti
# See LICENSE file for license

import pytest

from ipavagrant.config import IPAVagrantConfig, IPATopoConfig
from ipavagrant.constants import (
    DEFAULT_CONFIG_FILENAME,
    DEFAULT_TOPO_CONFIG_FILENAME,
    DEFAULT_CONFIG
)


@pytest.fixture(scope="module")
def default_config():
    return IPAVagrantConfig()


@pytest.fixture(scope="module")
def default_topo_config():
    return IPATopoConfig()


def test_default_config_file(default_config):
    assert default_config.get_filename() == DEFAULT_CONFIG_FILENAME


@pytest.mark.parametrize("key,val", DEFAULT_CONFIG.items())
def test_default_config_attrs(default_config, key, val):
    assert getattr(default_config, key) == val, "{} mistmatch".format(key)


def test_default_config_no_attr(default_config):
    with pytest.raises(AttributeError):
        assert default_config.nonexisting_attr


def test_default_config_extra_attr(default_config):
    for key in default_config.config.keys():
        assert key in DEFAULT_CONFIG, "{} is not defined".format(key)


def test_topo_default_config_file(default_topo_config):
    assert default_topo_config.get_filename() == DEFAULT_TOPO_CONFIG_FILENAME


def test_topo_default_get_topo(default_topo_config):
    assert default_topo_config.topologies
    assert default_topo_config.tests