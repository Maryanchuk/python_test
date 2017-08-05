# -*- coding: utf-8 -*-


import pytest
from group import Group
from application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return  fixture



def test_text_megic(app):


        app.login(username="tolikivanyuk@gmail.com", password="ihor198q")
        app.create_template(Group(listname="qqqq", Tmptext="wwwwww"))

def test_text_megic_empty(app):

            app.login(username="tolikivanyuk@gmail.com", password="ihor198q")
            app.create_template(Group(listname="", Tmptext=""))








