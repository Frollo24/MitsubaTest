import mitsuba as mi
import matplotlib.pyplot as plt


def test_editing_scene():
    mi.set_variant('cuda_ad_rgb')
    scene = mi.load_file('scenes/living-room-2/scene.xml')

    sensor_cam = mi.load_dict({
        'type': 'perspective',
        'to_world': mi.ScalarTransform4f.look_at(
            target=[-4.0, 0.0, 0.0],
            origin=[3.0, 0.5, 5.0],
            up=[0.0, 1.0, 0.0]
        ),
        'film': {'type': 'hdrfilm', 'width': 360, 'height': 640}
    })
    image = mi.render(scene, sensor=sensor_cam, spp=1024)
    
    plt.axis('off')
    plt.imshow(image ** (1.0 / 2.2))

    mi.util.write_bitmap('living_room_scene.png', image, quality=1)  # Avoids compression errors with PNG files
    mi.util.write_bitmap('living_room_scene.exr', image)


def test_render():
    mi.set_variant('cuda_ad_rgb')
    scene = mi.load_file('scenes/cbox.xml')
    image = mi.render(scene, spp=1024)

    plt.axis('off')
    plt.imshow(image ** (1.0 / 2.2))

    mi.util.write_bitmap('my_first_render.png', image)
    mi.util.write_bitmap('my_first_render.exr', image)


def print_mitsuba_variants():
    print(mi.variants())
