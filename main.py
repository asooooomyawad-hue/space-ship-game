def on_countdown_end():
    game.over(True, effects.smiles)
    music.magic_wand.play()
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    mySprite.start_effect(effects.fire, 2000)
    info.change_life_by(-1)
    otherSprite.destroy(effects.ashes, 10)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

othersprite: Sprite = None
mySprite: Sprite = None
scene.set_background_color(14)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . f . . . f . . . . . .
        . . . . f 6 f . f 6 f . . . . .
        . . . f 2 f 6 f 6 f 2 f . . . .
        . . . f f f f 6 f f f f . . . .
        . . . . f f f 6 f f f . . . . .
        . . . . f f f f f f f . . . . .
        . . . . f 2 f 6 f 2 f . . . . .
        . . . . . . 1 f 1 . . . . . . .
        . . . . . 2 . 1 . 2 . . . . . .
        . . . . . 2 . . . 2 . . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.start_countdown(30)
info.set_life(3)

def on_update_interval():
    global othersprite
    othersprite = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . e e f f e . .
            . . . . . . e e e e f f e e e .
            . . . . . e e e e e e e e e e .
            . . . . . e d d e e e c c e e .
            . . . e e e d e e e e c e e e .
            . . . e e e e e e f f e e e e .
            . . . e e c e e e f e e e e e .
            . . e e e e e e f f e e e e e .
            . . e e e d d e e e e f e f f .
            . . e e d d e e e e f f e f e .
            . . c c e e e e e e f e e e e .
            . . c e e e e c e e e e e e e .
            . . . e e e c c e e e d d e . .
            . . . . e e e d d e e d . . . .
            . . . . . e d d e . . . . . . .
            """),
        randint(-50, 50),
        randint(-50, 50))
game.on_update_interval(200, on_update_interval)
