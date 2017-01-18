# coding: utf-8
"""
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR

from .flask import app

db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(BIGINT(unsigned=True), primary_key=True)
    name = db.Column(VARCHAR(64), nullable=False)
    leader_id = db.Column(BIGINT, nullable=False)


class Department(db.Model):
    id = db.Column(BIGINT(unsigned=True), primary_key=True)
    leader_id = db.Column(BIGINT, nullable=False)


class Resource(db.Model):
    id = db.Column(BIGINT(unsigned=True), primary_key=True)
    name = db.Column(VARCHAR(64), nullable=False)


class Permission(db.Model):
    id = db.Column(BIGINT(unsigned=True), primary_key=True)
    resource_id = db.Column(BIGINT, nullable=False)
    action = db.Column(VARCHAR(64), nullable=False)
