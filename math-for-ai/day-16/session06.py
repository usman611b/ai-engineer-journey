# Ordinary Gradient Descent
x_gd = 5
learning_rate = 0.1

print("Ordinary Gradient Descent")

for step in range(5):
    gradient = 2 * x_gd
    x_gd = x_gd - learning_rate * gradient

    print("Step:", step + 1, "x:", round(x_gd, 4))


# Gradient Descent with Momentum
x_momentum = 5
velocity = 0
momentum = 0.9

print("\nMomentum")

for step in range(5):
    gradient = 2 * x_momentum

    velocity = momentum * velocity - learning_rate * gradient
    x_momentum = x_momentum + velocity

    print(
        "Step:", step + 1,
        "x:", round(x_momentum, 4),
        "velocity:", round(velocity, 4),
    )
"""
ugvuuh jh ughuvytfyusdrtyjnbxdrtyhbvxdrtyhvdt
ftyujty7ijht78ikjbgy89ok89olky89ok89okhy7
hghb vvh7rfghujkmncfrt678ijbvcrtyhdryhdr67ujbr567uhr67ijhgtytfvji87
hvcfthbvcfghb fghjm
"""