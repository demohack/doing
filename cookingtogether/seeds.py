"""Seed file to make sample data for pets db."""

from typing import ContextManager
from models import db, connect_db, Any_Type, Any_Value, Location, Entity_Group, Entity_Follow, Entity_Like, Entity, Post_Reply, Post, Event, Invite, Food, Recipe, Tool, Event_Item, Event_Signup, Recipe_Ingredient, Stock_Ingredient, Recipe_Tools, Stock_Tool
from app import create_app
connect_db(create_app())

# Create all tables

db.drop_all()
db.create_all()

t = post_type = Any_Type(name="post_type"); db.session.add(t); db.session.commit()
t = table_type = Any_Type(name="table_type"); db.session.add(t); db.session.commit()
t = entity_type = Any_Type(name="entity_type"); db.session.add(t); db.session.commit()
t = unit_type = Any_Type(name="unit_type"); db.session.add(t); db.session.commit()
t = category_type = Any_Type(name="category_type"); db.session.add(t); db.session.commit()
t = region_type = Any_Type(name="region_type"); db.session.add(t); db.session.commit()
t = tool_type = Any_Type(name="tool_type"); db.session.add(t); db.session.commit()

# post_type
t = any_post = Any_Value(name="post", any_type_id=post_type.id); db.session.add(t); db.session.commit()
t = any_discussion = Any_Value(name="discussion", any_type_id=post_type.id); db.session.add(t); db.session.commit()

# table_type
t = any_event = Any_Value(name="event", any_type_id=table_type.id); db.session.add(t); db.session.commit()
t = any_invite = Any_Value(name="invite", any_type_id=table_type.id); db.session.add(t); db.session.commit()
t = any_food = Any_Value(name="food", any_type_id=table_type.id); db.session.add(t); db.session.commit()
t = any_recipe = Any_Value(name="recipe", any_type_id=table_type.id); db.session.add(t); db.session.commit()
t = any_ingredient = Any_Value(name="ingredient", any_type_id=table_type.id); db.session.add(t); db.session.commit()

# entity_type
t = any_person = Any_Value(name="person", any_type_id=entity_type.id); db.session.add(t); db.session.commit()
t = any_group = Any_Value(name="group", any_type_id=entity_type.id); db.session.add(t); db.session.commit()
t = any_business = Any_Value(name="business", any_type_id=entity_type.id); db.session.add(t); db.session.commit()

# unit volume - imperial
t = Any_Value(name="cups", abbrev="c", any_type_id=unit_type.id); db.session.add(t); db.session.commit()
t = Any_Value(name="tablespoons", abbrev="tbsp", any_type_id=unit_type.id); db.session.add(t); db.session.commit()
t = Any_Value(name="teaspoons", abbrev="tsp", any_type_id=unit_type.id); db.session.add(t); db.session.commit()
t = Any_Value(name="quarts", abbrev="qt", any_type_id=unit_type.id); db.session.add(t); db.session.commit()
t = Any_Value(name="pints", abbrev="pt", any_type_id=unit_type.id); db.session.add(t); db.session.commit()
t = Any_Value(name="gallons", abbrev="gal", any_type_id=unit_type.id); db.session.add(t); db.session.commit()

# unit volume - metric
t = Any_Value(name="milliliters", abbrev="ml", any_type_id=unit_type.id); db.session.add(t); db.session.commit()
t = Any_Value(name="liters", abbrev="l", any_type_id=unit_type.id); db.session.add(t); db.session.commit()

# unit weight
t = Any_Value(name="ounces", abbrev="oz", any_type_id=unit_type.id); db.session.add(t); db.session.commit()
t = Any_Value(name="fluid ounces", abbrev="fl oz", any_type_id=unit_type.id); db.session.add(t); db.session.commit()
t = Any_Value(name="pounds", abbrev="lb", any_type_id=unit_type.id); db.session.add(t); db.session.commit()
t = Any_Value(name="kilograms", abbrev="kg", any_type_id=unit_type.id); db.session.add(t); db.session.commit()

# unit energy
t = Any_Value(name="calories", abbrev="kcal", any_type_id=unit_type.id); db.session.add(t); db.session.commit()

# category
t = f_group = Any_Value(name="food group", any_type_id=category_type.id); db.session.add(t); db.session.commit()
t = f_menu = Any_Value(name="food menu", any_type_id=category_type.id); db.session.add(t); db.session.commit()
t = f_dish = Any_Value(name="food dish", any_type_id=category_type.id); db.session.add(t); db.session.commit()
t = f_item = Any_Value(name="food item", any_type_id=category_type.id); db.session.add(t); db.session.commit()

# region
t = r_souther = Any_Value(name="southern", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_polynesian = Any_Value(name="polynesian", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_mediterranean = Any_Value(name="mediterranean", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_ethiopian = Any_Value(name="Ethiopian", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_moroccan = Any_Value(name="Moroccan", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_french = Any_Value(name="French", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_italian = Any_Value(name="Italian", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_greek = Any_Value(name="Greek", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_spanish = Any_Value(name="Spanish", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_mexiacan = Any_Value(name="Mexican", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_american = Any_Value(name="American", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_native_american = Any_Value(name="Native American", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_cambodian = Any_Value(name="Cambodian", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_chinese = Any_Value(name="Chinese", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_filipino = Any_Value(name="Filipino", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_indian = Any_Value(name="Indian", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_japanese = Any_Value(name="Japanese", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_korean = Any_Value(name="Korean", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_taiwanese = Any_Value(name="Taiwanese", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_thai = Any_Value(name="Thai", any_type_id=region_type.id); db.session.add(t); db.session.commit()
t = r_vietnamese = Any_Value(name="Vietnamese", any_type_id=region_type.id); db.session.add(t); db.session.commit()

# tool
t = t_utensil = Any_Value(name="eating utensil", any_type_id=tool_type.id); db.session.add(t); db.session.commit()
t = t_tableware = Any_Value(name="tableware", any_type_id=tool_type.id); db.session.add(t); db.session.commit()
t = t_cookingware = Any_Value(name="cooking ware", any_type_id=tool_type.id); db.session.add(t); db.session.commit()
t = t_equipment = Any_Value(name="equipment", any_type_id=tool_type.id); db.session.add(t); db.session.commit()
t = t_furniture = Any_Value(name="furniture", any_type_id=tool_type.id); db.session.add(t); db.session.commit()

e = l1 = Location(name="biz", street="1234 NE 2nd Ave", city="Portland", state="OR", zip="97213"); db.session.add(e); db.session.commit()
e = l2 = Location(name="biz", street="123 NE Sandy Blvd", city="Portland", state="OR", zip="97218"); db.session.add(e); db.session.commit()
e = l3 = Location(name="biz", street="555 NE Broadway", city="Portland", state="OR", zip="97213"); db.session.add(e); db.session.commit()
e = l4 = Location(name="home", street="9999 NE 4th Ave", city="Portland", state="OR", zip="97218"); db.session.add(e); db.session.commit()
e = l5 = Location(name="home", street="29 NE 6th Ave", city="Portland", state="OR", zip="97218"); db.session.add(e); db.session.commit()
e = l6 = Location(name="home", street="88 NE 23rd Ave", city="Portland", state="OR", zip="97218"); db.session.add(e); db.session.commit()

e = ep1 = Entity(name="Yu", entity_type_id=any_person.id, location_id=l4.id); db.session.add(e); db.session.commit()
e = ep2 = Entity(name="Yuki", entity_type_id=any_person.id, location_id=l4.id); db.session.add(e); db.session.commit()
e = ep3 = Entity(name="Tom", entity_type_id=any_person.id, location_id=l5.id); db.session.add(e); db.session.commit()
e = ep4 = Entity(name="Penelope", entity_type_id=any_person.id, location_id=l6.id); db.session.add(e); db.session.commit()

e = eb1 = Entity(name="Foot Traffic", entity_type_id=any_group.id, location_id=l1.id); db.session.add(e); db.session.commit()
e = eb2 = Entity(name="Mekong Bistro", entity_type_id=any_group.id, location_id=l2.id); db.session.add(e); db.session.commit()
e = eb3 = Entity(name="Chopsticks Karaoke", entity_type_id=any_group.id, location_id=l3.id); db.session.add(e); db.session.commit()

e = Entity_Group(entity_id=ep1.id, group_id=eb1.id, is_admin=True); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep1.id, group_id=eb2.id, is_member=True); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep2.id, group_id=eb1.id, is_admin=True); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep2.id, group_id=eb2.id, is_member=True); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep3.id, group_id=eb1.id, is_premier=True); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep3.id, group_id=eb1.id, is_premier=True); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep4.id, group_id=eb1.id, is_banned=True); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep4.id, group_id=eb2.id, is_banned=True); db.session.add(e); db.session.commit()

e = Entity_Group(entity_id=ep1.id, group_id=ep2.id); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep1.id, group_id=ep3.id); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep1.id, group_id=ep4.id); db.session.add(e); db.session.commit()
e = Entity_Group(entity_id=ep1.id, group_id=eb1.id); db.session.add(e); db.session.commit()

e = p1 = Post(title="test", content="test content", author_id=ep1.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p2 = Post(title="test 2", content="test 2 content", author_id=ep1.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p3 = Post(title="test 3", content="test 3 content", author_id=eb1.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p4 = Post(title="test 4", content="test 4 content", author_id=eb2.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p5 = Post(title="test 5", content="test 5 content", author_id=eb3.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p6 = Post(title="test 6", content="test 6 content", author_id=eb1.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p7 = Post(title="test 7", content="test 7 content", author_id=eb2.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p8 = Post(title="test 8", content="test 8 content", author_id=ep2.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p9 = Post(title="test 9", content="test 9 content", author_id=ep3.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p10 = Post(title="test 10", content="test 10 content", author_id=ep4.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p11 = Post(title="test 11", content="test 11 content", author_id=ep1.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()
e = p12 = Post(title="test 12", content="test 12 content", author_id=ep2.id, post_type_id=any_post.id); db.session.add(e); db.session.commit()

e = Entity_Follow(entity_id=ep1.id, follows_id=ep2.id); db.session.add(e); db.session.commit()
e = Entity_Follow(entity_id=ep1.id, follows_id=ep3.id); db.session.add(e); db.session.commit()
e = Entity_Follow(entity_id=ep1.id, follows_id=ep4.id); db.session.add(e); db.session.commit()
e = Entity_Follow(entity_id=ep1.id, follows_id=eb1.id); db.session.add(e); db.session.commit()

e = Entity_Like(entity_id=ep1.id, post_id=p1.id); db.session.add(e); db.session.commit()
e = Entity_Like(entity_id=ep1.id, post_id=p2.id); db.session.add(e); db.session.commit()
e = Entity_Like(entity_id=ep1.id, post_id=p3.id); db.session.add(e); db.session.commit()
e = Entity_Like(entity_id=ep1.id, post_id=p4.id); db.session.add(e); db.session.commit()
e = Entity_Like(entity_id=ep2.id, post_id=p2.id); db.session.add(e); db.session.commit()
e = Entity_Like(entity_id=ep2.id, post_id=p5.id); db.session.add(e); db.session.commit()
e = Entity_Like(entity_id=ep3.id, post_id=p6.id); db.session.add(e); db.session.commit()
e = Entity_Like(entity_id=ep3.id, post_id=p7.id); db.session.add(e); db.session.commit()
e = Entity_Like(entity_id=ep3.id, post_id=p8.id); db.session.add(e); db.session.commit()

e = Post_Reply(post_id=p1.id, reply_id=p2.id); db.session.add(e); db.session.commit()
e = Post_Reply(post_id=p1.id, reply_id=p3.id); db.session.add(e); db.session.commit()
e = Post_Reply(post_id=p1.id, reply_id=p4.id); db.session.add(e); db.session.commit()
e = Post_Reply(post_id=p2.id, reply_id=p5.id); db.session.add(e); db.session.commit()
e = Post_Reply(post_id=p2.id, reply_id=p6.id); db.session.add(e); db.session.commit()
e = Post_Reply(post_id=p3.id, reply_id=p7.id); db.session.add(e); db.session.commit()
e = Post_Reply(post_id=p5.id, reply_id=p8.id); db.session.add(e); db.session.commit()
e = Post_Reply(post_id=p8.id, reply_id=p9.id); db.session.add(e); db.session.commit()

e = e1 = Event(title="Karaoke Party", content="Kick it at Chopsticks", event_date="10/31/2021", location_id=l3.id, organized_by_id=ep1.id); db.session.add(e); db.session.commit()
e = e2 = Event(title="Ramen Party", content="Learn to make ramen together", event_date="10/31/2021", location_id=l1.id, organized_by_id=ep2.id); db.session.add(e); db.session.commit()
e = e3 = Event(title="Beef Soup", content="Bring your beef soup recipes", event_date="10/31/2021", location_id=l2.id, organized_by_id=ep3.id); db.session.add(e); db.session.commit()
e = e4 = Event(title="Pho Night", content="Lets make pho!", event_date="10/31/2021", location_id=l5.id, organized_by_id=ep2.id); db.session.add(e); db.session.commit()

e = i1 = Invite(sender_id=ep1.id, receiver_id=ep2.id, add_invites=4, event_id=e1.id); db.session.add(e); db.session.commit()
e = i2 = Invite(sender_id=ep1.id, receiver_id=ep3.id, add_invites=4, event_id=e1.id); db.session.add(e); db.session.commit()
e = i3 = Invite(sender_id=ep1.id, receiver_id=ep4.id, add_invites=4, event_id=e1.id); db.session.add(e); db.session.commit()
e = i4 = Invite(sender_id=ep2.id, receiver_id=ep3.id, add_invites=4, event_id=e1.id); db.session.add(e); db.session.commit()
e = i5 = Invite(sender_id=ep2.id, receiver_id=ep4.id, add_invites=4, event_id=e1.id); db.session.add(e); db.session.commit()
e = i6 = Invite(sender_id=ep3.id, receiver_id=ep4.id, add_invites=4, event_id=e1.id); db.session.add(e); db.session.commit()
e = i7 = Invite(sender_id=ep1.id, receiver_id=ep2.id, add_invites=4, event_id=e2.id); db.session.add(e); db.session.commit()
e = i8 = Invite(sender_id=ep1.id, receiver_id=ep3.id, add_invites=4, event_id=e2.id); db.session.add(e); db.session.commit()
e = i9 = Invite(sender_id=ep1.id, receiver_id=ep4.id, add_invites=4, event_id=e2.id); db.session.add(e); db.session.commit()
e = i10 = Invite(sender_id=ep2.id, receiver_id=ep3.id, add_invites=4, event_id=e3.id); db.session.add(e); db.session.commit()
e = i11 = Invite(sender_id=ep2.id, receiver_id=ep4.id, add_invites=4, event_id=e3.id); db.session.add(e); db.session.commit()
e = i12 = Invite(sender_id=ep3.id, receiver_id=ep4.id, add_invites=4, event_id=e3.id); db.session.add(e); db.session.commit()

e = f1 = Food(name="papaya salad", category_type_id=f_dish.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = f2 = Food(name="tom yum soup", category_type_id=f_dish.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = f3 = Food(name="pad thai", category_type_id=f_dish.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = f4 = Food(name="red curry", category_type_id=f_dish.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = f5 = Food(name="banh mi sandwich", category_type_id=f_dish.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = f6 = Food(name="salad rolls", category_type_id=f_dish.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = f7 = Food(name="fried rice", category_type_id=f_dish.id, region_type_id=r_cambodian.id, author_id=ep1.id); db.session.add(e); db.session.commit()

e = r1 = Recipe(name="Yu's salad rolls", category_type_id=f_dish.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = r2 = Recipe(name="Yu's tom yum soup", category_type_id=f_dish.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = r3 = Recipe(name="Yuki's pad thai", category_type_id=f_dish.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = r4 = Recipe(name="Yu's red curry", category_type_id=f_dish.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = r5 = Recipe(name="Yuki's banh mi sandwich", category_type_id=f_dish.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = r6 = Recipe(name="Yu's papaya salad", category_type_id=f_dish.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = r7 = Recipe(name="Yuki's fried rice", category_type_id=f_dish.id, region_type_id=r_cambodian.id, author_id=ep1.id); db.session.add(e); db.session.commit()

e = i1 = Food(name="bread", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i2 = Food(name="rice noodle", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i3 = Food(name="rice paper", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i4 = Food(name="papaya", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i5 = Food(name="carrots", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i6 = Food(name="lettuce", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i7 = Food(name="bean sprouts", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i8 = Food(name="fish mint", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i9 = Food(name="shiso", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i10 = Food(name="pork", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i11 = Food(name="green beans", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i12 = Food(name="tofu", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i13 = Food(name="fish sauce", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i14 = Food(name="lime", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i15 = Food(name="garlic", category_type_id=f_item.id, region_type_id=r_cambodian.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i16 = Food(name="green onion", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i17 = Food(name="chili peppers", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()

e = i18 = Food(name="glass noodle", category_type_id=f_item.id, region_type_id=r_cambodian.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i19 = Food(name="onion", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i20 = Food(name="cilantro", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i21 = Food(name="spearmint", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i22 = Food(name="pepper mint", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i23 = Food(name="kale", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i24 = Food(name="tomatoes", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i25 = Food(name="sorrel", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i26 = Food(name="sweet peas", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i27 = Food(name="green beens", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i28 = Food(name="chicken", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i29 = Food(name="beef", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i30 = Food(name="eggs", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i31 = Food(name="seaweed", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i32 = Food(name="rice", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i33 = Food(name="bell peppers", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i34 = Food(name="grapes", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()

e = i35 = Food(name="apple", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i36 = Food(name="pear", category_type_id=f_item.id, region_type_id=r_thai.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i37 = Food(name="strawberries", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i38 = Food(name="mustard greens", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i39 = Food(name="cabbage", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i40 = Food(name="daikon radish", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i41 = Food(name="arigula", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i42 = Food(name="spinach", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i43 = Food(name="corn", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()
e = i44 = Food(name="collards", category_type_id=f_item.id, region_type_id=r_vietnamese.id, author_id=ep1.id); db.session.add(e); db.session.commit()

e = t1 = Tool(name="chef's knife", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()
e = t2 = Tool(name="santoku knife", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()
e = t3 = Tool(name="kitchen shears", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()
e = t4 = Tool(name="bread knife", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()
e = t5 = Tool(name="cleaver knife", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()
e = t6 = Tool(name="paring knife", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()
e = t7 = Tool(name="julienne peeler", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()

e = t8 = Tool(name="steak knife", tool_type_id=t_tableware.id); db.session.add(e); db.session.commit()
e = t9 = Tool(name="chopsticks", tool_type_id=t_tableware.id); db.session.add(e); db.session.commit()

e = t10 = Tool(name="large pot", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()
e = t11 = Tool(name="rice cooker", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()
e = t12 = Tool(name="teapot", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()
e = t13 = Tool(name="frying pan", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()

e = t14 = Tool(name="cutting board", tool_type_id=t_cookingware.id); db.session.add(e); db.session.commit()

e = t15 = Tool(name="sake cup", tool_type_id=t_tableware.id); db.session.add(e); db.session.commit()
e = t16 = Tool(name="small bowl", tool_type_id=t_tableware.id); db.session.add(e); db.session.commit()
e = t17 = Tool(name="large bowl", tool_type_id=t_tableware.id); db.session.add(e); db.session.commit()
e = t18 = Tool(name="salad bowl", tool_type_id=t_tableware.id); db.session.add(e); db.session.commit()
e = t19 = Tool(name="salad plate", tool_type_id=t_tableware.id); db.session.add(e); db.session.commit()
e = t20 = Tool(name="12 by 1 inch bowl", tool_type_id=t_tableware.id); db.session.add(e); db.session.commit()

e = ei1 = Event_Item(event_id=e1.id, food_id=f6.id, recipe_id=r1.id); db.session.add(e); db.session.commit()

e = ei1 = Event_Signup(event_id=e1.id, food_id=f6.id, recipe_id=r1.id, signer_id=e1.id); db.session.add(e); db.session.commit()
e = ei1 = Event_Signup(event_id=e1.id, food_id=f6.id, recipe_id=r1.id, signer_id=e2.id); db.session.add(e); db.session.commit()

e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i2.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i3.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i5.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i6.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i7.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i8.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i9.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i10.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i11.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i12.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i13.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i14.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i15.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i16.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i17.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i24.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i25.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i33.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i34.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i37.id); db.session.add(e); db.session.commit()
e = ri1 = Recipe_Ingredient(recipe_id=r1.id, ingredient_id=i41.id); db.session.add(e); db.session.commit()

e = rt1 = Recipe_Tools(recipe_id=r1.id, tool_id=t1.id); db.session.add(e); db.session.commit()
e = rt2 = Recipe_Tools(recipe_id=r1.id, tool_id=t7.id); db.session.add(e); db.session.commit()
e = rt3 = Recipe_Tools(recipe_id=r1.id, tool_id=t9.id); db.session.add(e); db.session.commit()
e = rt4 = Recipe_Tools(recipe_id=r1.id, tool_id=t10.id); db.session.add(e); db.session.commit()
e = rt5 = Recipe_Tools(recipe_id=r1.id, tool_id=t14.id); db.session.add(e); db.session.commit()
e = rt6 = Recipe_Tools(recipe_id=r1.id, tool_id=t16.id); db.session.add(e); db.session.commit()
e = rt7 = Recipe_Tools(recipe_id=r1.id, tool_id=t17.id); db.session.add(e); db.session.commit()
e = rt8 = Recipe_Tools(recipe_id=r1.id, tool_id=t18.id); db.session.add(e); db.session.commit()
e = rt9 = Recipe_Tools(recipe_id=r1.id, tool_id=t19.id); db.session.add(e); db.session.commit()
e = rt10 = Recipe_Tools(recipe_id=r1.id, tool_id=t20.id); db.session.add(e); db.session.commit()

e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i2.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i3.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i5.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i6.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i7.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i8.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i9.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i10.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i11.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i12.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i13.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i14.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i15.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i16.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i17.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i24.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i25.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i33.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i34.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i37.id); db.session.add(e); db.session.commit()
e = si1 = Stock_Ingredient(owner_id=ep1.id, ingredient_id=i41.id); db.session.add(e); db.session.commit()

e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t1.id); db.session.add(e); db.session.commit()
e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t7.id); db.session.add(e); db.session.commit()
e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t9.id); db.session.add(e); db.session.commit()
e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t10.id); db.session.add(e); db.session.commit()
e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t14.id); db.session.add(e); db.session.commit()
e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t16.id); db.session.add(e); db.session.commit()
e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t17.id); db.session.add(e); db.session.commit()
e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t18.id); db.session.add(e); db.session.commit()
e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t19.id); db.session.add(e); db.session.commit()
e = st1 = Stock_Tool(owner_id=ep1.id, tool_id=t20.id); db.session.add(e); db.session.commit()