"""Models for Cooking app."""

# import ipdb; ipdb.set_trace()

from datetime import datetime

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Any_Type(db.Model):
    """Any_Type: one of { post_type, table_type, entity_type, unit_type, category_type, region_type, tool_type }"""
    __tablename__ = 'any_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.name}>"


class Any_Value(db.Model):
    """Any_Value: one of { dining, cooking, prepping, cleaning, etc }"""
    __tablename__ = 'any_value'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text)
    abbrev = db.Column(db.Text)
    description = db.Column(db.Text)
    any_type_id = db.Column(db.Integer, db.ForeignKey('any_type.id'))

    any_type = db.relationship("Any_Type", primaryjoin=(Any_Type.id == any_type_id), backref="values")

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.name}>"


class Location(db.Model):
    """Location"""
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)

    street = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip = db.Column(db.Text)

    has_kitchen = db.Column(db.Boolean)
    has_restroom = db.Column(db.Boolean)
    has_wifi = db.Column(db.Boolean)
    indoor_capacity = db.Column(db.Integer)
    outdoor_capacity = db.Column(db.Integer)
    rooms = db.Column(db.Integer)

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.name}>"


class Entity_Group(db.Model):
    """Entity_Group"""
    __tablename__ = 'entity_group'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'))   # user that does the following
    group_id = db.Column(db.Integer, db.ForeignKey('entity.id'))    # user that is followed

    is_admin = db.Column(db.Boolean, default=False)
    is_premier = db.Column(db.Boolean, default=False)
    is_member = db.Column(db.Boolean, default=False)
    is_subscribed = db.Column(db.Boolean, default=True)
    is_banned = db.Column(db.Boolean, default=False)
    is_enabled = db.Column(db.Boolean, default=True)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.entity_id} {s.group_id}>"


class Entity_Follow(db.Model):
    """Entity_Follow"""
    __tablename__ = "entity_follow"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    follows_id = db.Column(db.Integer, db.ForeignKey('entity.id'))  # user that is followed
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'))   # user that does the following

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.entity_id} {s.follows_id}>"


class Entity_Like(db.Model):
    """Entity_Like"""
    __tablename__ = "entity_like"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.entity_id} {s.like_id}>"


class Entity(db.Model):
    """Entity: a specific person, role, group, table, row"""
    __tablename__ = 'entity'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)

    username = db.Column(db.Text)
    hashed_pwd = db.Column(db.Text)

    email = db.Column(db.Text)
    phone = db.Column(db.Text)
    site_url = db.Column(db.Text)

    entity_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    image_url = db.Column(db.Text)

    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    can_call = db.Column(db.Boolean, default=True)
    can_text = db.Column(db.Boolean, default=True)
    can_email = db.Column(db.Boolean, default=True)

    joined_date = db.Column(db.DateTime)

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)

    is_enabled = db.Column(db.Boolean, default=True)
    is_deleted = db.Column(db.Boolean, default=False)

    entity_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == entity_type_id))
    location = db.relationship("Location", primaryjoin=(Location.id == location_id))

    likes = db.relationship(
        "Post",
        secondary="entity_like",
        primaryjoin=(Entity_Like.entity_id == id),
        secondaryjoin=("Entity_Like.post_id == Post.id")
    )

    members = db.relationship(                          # alias: followers
        "Entity",
        secondary="entity_group",
        primaryjoin=(Entity_Group.group_id == id),      # user that is followed
        secondaryjoin=(Entity_Group.entity_id == id)    # user that does the following
    )

    groups = db.relationship(                           # alias: following
        "Entity",
        secondary="entity_group",
        primaryjoin=(Entity_Group.entity_id == id),     # user that does the following
        secondaryjoin=(Entity_Group.group_id == id)     # user that is followed
    )

    followers = db.relationship(
        "Entity",
        secondary="entity_follow",
        primaryjoin=(Entity_Follow.follows_id == id),   # user that is followed
        secondaryjoin=(Entity_Follow.entity_id == id)   # user that does the following
    )

    following = db.relationship(
        "Entity",
        secondary="entity_follow",
        primaryjoin=(Entity_Follow.entity_id == id),    # user that does the following
        secondaryjoin=(Entity_Follow.follows_id == id)  # user that is followed
    )

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.name} {s.created_date} {s.joined_date}>"


class Post_Reply(db.Model):
    """Post_Reply"""
    __tablename__ = 'post_reply'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    reply_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.post_id} {s.reply_id}>"


class Post(db.Model):
    """Post"""
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.Text)
    content = db.Column(db.Text)

    post_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    sent_date = db.Column(db.DateTime)
    read_date = db.Column(db.DateTime)
    sender_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    is_enabled = db.Column(db.Boolean, default=True)
    is_deleted = db.Column(db.Boolean, default=False)

    table_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))
    row_id = db.Column(db.Integer)

    post_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == post_type_id))
    author = db.relationship("Entity", primaryjoin=(Entity.id == author_id))
    editor = db.relationship("Entity", primaryjoin=(Entity.id == editor_id))
    sender = db.relationship("Entity", primaryjoin=(Entity.id == sender_id))
    receiver = db.relationship("Entity", primaryjoin=(Entity.id == receiver_id))
    table = db.relationship("Any_Value", primaryjoin=(Any_Value.id == table_id))

    replies = db.relationship(
        "Post",
        secondary="post_reply",
        primaryjoin=(Post_Reply.post_id == id),
        secondaryjoin=(Post_Reply.reply_id == id)
    )

    parent = db.relationship(
        "Post",
        secondary="post_reply",
        primaryjoin=(Post_Reply.reply_id == id),
        secondaryjoin=(Post_Reply.post_id == id)
    )

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.title} {s.author_id} {s.created_date}>"


class Event(db.Model):
    """Event"""
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.Text)
    content = db.Column(db.Text)

    event_date = db.Column(db.DateTime)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    organized_by_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    audience_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    discussion_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    location = db.relationship("Location", primaryjoin=(Location.id == location_id))
    author = db.relationship("Entity", primaryjoin=(Entity.id == author_id), backref="events_authored")
    editor = db.relationship("Entity", primaryjoin=(Entity.id == editor_id), backref="events_edited")
    organized_by = db.relationship("Entity", primaryjoin=(Entity.id == organized_by_id), backref="events_organized")
    organized_for = db.relationship("Entity", primaryjoin=(Entity.id == audience_id))
    discussion = db.relationship("Post", primaryjoin=(Post.id == discussion_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.title} {s.event_date}>"


class Invite(db.Model):
    """Invite"""
    __tablename__ = 'invite'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    invite_code = db.Column(db.Text)

    title = db.Column(db.Text)
    content = db.Column(db.Text)

    sent_date = db.Column(db.DateTime)
    read_date = db.Column(db.DateTime)
    sender_id = db.Column(db.Integer, db.ForeignKey('entity.id', name="sender_invite_id_fkey"))
    receiver_id = db.Column(db.Integer, db.ForeignKey('entity.id', name="receiver_invite_id_fkey"))

    add_invites = db.Column(db.Integer) # can additionally invite 0, 1, or more

    accepted_date = db.Column(db.DateTime)

    discussion_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    event = db.relationship("Event", primaryjoin=(Event.id == event_id), backref="invites")
    sender = db.relationship("Entity", primaryjoin=(Entity.id == sender_id), backref="invites_sent")
    receiver = db.relationship("Entity", primaryjoin=(Entity.id == receiver_id), backref="invites_received")
    discussion = db.relationship("Post", primaryjoin=(Post.id == discussion_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.event_id} {s.sender_id} {s.receiver_id}>"


class Food(db.Model):
    """Food"""
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)

    category_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))
    region_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    background = db.Column(db.Text)
    nutrition = db.Column(db.Text)
    image_url = db.Column(db.Text)

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    discussion_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    category_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == category_type_id))
    region_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == region_type_id))
    author = db.relationship("Entity", primaryjoin=(Entity.id == author_id), backref="food_authored")
    editor = db.relationship("Entity", primaryjoin=(Entity.id == editor_id), backref="food_edited")
    discussion = db.relationship("Post", primaryjoin=(Post.id == discussion_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.name}>"

class Recipe(db.Model):
    """Recipe"""
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)

    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    category_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))
    region_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    background = db.Column(db.Text)
    nutrition = db.Column(db.Text)
    image_url = db.Column(db.Text)

    instruction_id = db.Column(db.Text)

    prep_time = db.Column(db.Integer)       # minutes
    cooking_time = db.Column(db.Integer)    # minutes
    servings = db.Column(db.Integer)

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    discussion_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    food = db.relationship("Food", primaryjoin=(Food.id == food_id))
    category_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == category_type_id))
    region_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == region_type_id))
    author = db.relationship("Entity", primaryjoin=(Entity.id == author_id), backref="recipe_authored")
    editor = db.relationship("Entity", primaryjoin=(Entity.id == editor_id), backref="recipe_edited")
    discussion = db.relationship("Post", primaryjoin=(Post.id == discussion_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.name}>"


class Tool(db.Model):
    """Tool"""
    __tablename__ = 'tool'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)

    tool_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    discussion_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    tool_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == tool_type_id))
    author = db.relationship("Entity", primaryjoin=(Entity.id == author_id), backref="tool_authored")
    editor = db.relationship("Entity", primaryjoin=(Entity.id == editor_id), backref="tool_edited")
    discussion = db.relationship("Post", primaryjoin=(Post.id == discussion_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.name}>"


class Event_Item(db.Model):
    """Event_Item"""
    __tablename__ = 'event_item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

    title = db.Column(db.Text)
    content = db.Column(db.Text)

    hours = db.Column(db.Numeric)
    dollars = db.Column(db.Numeric)

    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    amount = db.Column(db.Numeric)
    unit_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'))
    tool_qty = db.Column(db.Numeric)

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    discussion_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    event = db.relationship("Event", primaryjoin=(Event.id == event_id), backref="items")
    food = db.relationship("Food", primaryjoin=(Food.id == food_id))
    recipe = db.relationship("Recipe", primaryjoin=(Recipe.id == recipe_id))
    unit_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == unit_type_id))
    tool = db.relationship("Tool", primaryjoin=(Tool.id == tool_id))
    author = db.relationship("Entity", primaryjoin=(Entity.id == author_id))
    editor = db.relationship("Entity", primaryjoin=(Entity.id == editor_id))
    discussion = db.relationship("Post", primaryjoin=(Post.id == discussion_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.event_id} hrs {s.title}>"


class Event_Signup(db.Model):
    """Event_Signup"""
    __tablename__ = 'event_signup'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event_item_id = db.Column(db.Integer, db.ForeignKey('event_item.id'))

    signer_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    signup_date = db.Column(db.DateTime)

    comment = db.Column(db.Text)

    hours = db.Column(db.Numeric)
    dollars = db.Column(db.Numeric)

    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    amount = db.Column(db.Numeric)
    unit_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'))
    tool_qty = db.Column(db.Numeric)

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    discussion_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    event = db.relationship("Event", primaryjoin=(Event.id == event_id), backref="signups")
    event_item = db.relationship("Event_Item", primaryjoin=(Event_Item.id == event_item_id))
    signer = db.relationship("Entity", primaryjoin=(Entity.id == signer_id), backref="events_signedup")
    food = db.relationship("Food", primaryjoin=(Food.id == food_id))
    recipe = db.relationship("Recipe", primaryjoin=(Recipe.id == recipe_id))
    unit_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == unit_type_id))
    tool = db.relationship("Tool", primaryjoin=(Tool.id == tool_id))
    author = db.relationship("Entity", primaryjoin=(Entity.id == author_id))
    editor = db.relationship("Entity", primaryjoin=(Entity.id == editor_id))
    discussion = db.relationship("Post", primaryjoin=(Post.id == discussion_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.id} {s.event_id} {s.event_item_id} hrs {s.hours} ${s.dollars}>"


class Recipe_Ingredient(db.Model):
    """Recipe_Ingredient"""
    __tablename__ = 'recipe_ingredient'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('food.id'), primary_key=True)

    amount = db.Column(db.Numeric)
    unit_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    discussion_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    recipe = db.relationship("Recipe", primaryjoin=(Recipe.id == recipe_id), backref="uses_ingredients")
    food = db.relationship("Food", primaryjoin=(Food.id == ingredient_id), backref="used_in_recipes")
    unit_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == unit_type_id))
    author = db.relationship("Entity", primaryjoin=(Entity.id == author_id))
    editor = db.relationship("Entity", primaryjoin=(Entity.id == editor_id))
    discussion = db.relationship("Post", primaryjoin=(Post.id == discussion_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.recipe_id} {s.ingredient_id}>"


class Recipe_Tools(db.Model):
    """Recipe_Tools"""
    __tablename__ = 'recipe_tools'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'), primary_key=True)

    units = db.Column(db.Integer)
    unit_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    created_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    editor_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    discussion_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    recipe = db.relationship("Recipe", primaryjoin=(Recipe.id == recipe_id), backref="uses_tools")
    tool = db.relationship("Tool", primaryjoin=(Tool.id == tool_id), backref="used_in_recipes")
    unit_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == unit_type_id))
    author = db.relationship("Entity", primaryjoin=(Entity.id == author_id))
    editor = db.relationship("Entity", primaryjoin=(Entity.id == editor_id))
    discussion = db.relationship("Post", primaryjoin=(Post.id == discussion_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.recipe_id} {s.tool_id}>"


class Stock_Ingredient(db.Model):
    """Stock_Ingredient"""
    __tablename__ = 'stock_ingredient'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    owner_id = db.Column(db.Integer, db.ForeignKey('entity.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('food.id'), primary_key=True)

    amount = db.Column(db.Numeric)
    unit_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    owner = db.relationship("Entity", primaryjoin=(Entity.id == owner_id))
    food = db.relationship("Food", primaryjoin=(Food.id == ingredient_id))
    unit_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == unit_type_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.owner_id} {s.ingredient_id}>"


class Stock_Tool(db.Model):
    """Stock_Tool"""
    __tablename__ = 'stock_tool'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    owner_id = db.Column(db.Integer, db.ForeignKey('entity.id'), primary_key=True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'), primary_key=True)

    units = db.Column(db.Integer)
    unit_type_id = db.Column(db.Integer, db.ForeignKey('any_value.id'))

    owner = db.relationship("Entity", primaryjoin=(Entity.id == owner_id))
    tool = db.relationship("Tool", primaryjoin=(Tool.id == tool_id))
    unit_type = db.relationship("Any_Value", primaryjoin=(Any_Value.id == unit_type_id))

    def __repr__(s) -> str:
        return f"<{s.__tablename__} {s.owner_id} {s.tool_id}>"


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)
