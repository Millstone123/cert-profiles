from certprofiles.checker import check_profiles


def test_sample_profiles():
    assert check_profiles("profiles") == []
