info.onCountdownEnd(function on_countdown_end() {
    game.over(true, effects.smiles)
    music.magicWand.play()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    mySprite.startEffect(effects.fire, 2000)
    info.changeLifeBy(-1)
    otherSprite.destroy(effects.ashes, 10)
})
let othersprite : Sprite = null
let mySprite : Sprite = null
scene.setBackgroundColor(14)
mySprite = sprites.create(img`
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
        `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
mySprite.setFlag(SpriteFlag.StayInScreen, true)
info.startCountdown(30)
info.setLife(3)
game.onUpdateInterval(200, function on_update_interval() {
    
    othersprite = sprites.createProjectileFromSide(img`
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
            `, randint(-50, 50), randint(-50, 50))
})
