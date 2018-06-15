world = {
    'start_room':{
        'text':'You were walking in the mountians with your friend\nwhen you fell down a mineshaft. You \nplummeted for a munite untill you splashed down in\nan underwater pond. You swam to shore,\nand you find yourself in a large cavern.',
        'exits':{
            'rickety ladder':'surface',
            'mineshaft':'mineshaft',
            'door':'room'
        }
    },
    'surface':{
        'text':'You climb to the surface, your friend looks shocked to see you sruvived the fall.\nYour friend is part of the assassians guild, your \nfriend stabs you in the kidneys and throws you back\ndown the shaft!',
        'exits':{
            'q':'end'
        }
    },
    'mineshaft':{
        'text':'you went down a mineshaft, theres nothing for you here silly goose!',
        'exits':{
            'back':'start_room'
        }
    },
    'room':{
        'text':'You can see infront of you a wall covered in pickaxes, but not much more',
        'exits':{
            'back':'start_room'
        }
    }
}
