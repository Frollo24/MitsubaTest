import mitsuba as mi
import matplotlib.pyplot as plt

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
