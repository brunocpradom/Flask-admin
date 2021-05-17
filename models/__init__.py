# -*- coding: utf-8 -*-
import uuid
from sqlalchemy.dialects.postgresql import UUID
from extensions.extensions import db


class IdMixin(object):

    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)