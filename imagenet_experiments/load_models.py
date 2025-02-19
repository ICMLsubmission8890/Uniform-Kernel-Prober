import os
import torch
import torchvision.models as models

pretrained = True

suff = "_pretrained"
models_folder = "/content/drive/MyDrive/UKP/imagenet_experiments/models"
numcopies = 10
if pretrained:
    numcopies = 1

for i in range(numcopies):
    if not pretrained:
        suff = f"_untrained{i+1}"
    
    resnet18 = models.resnet18(pretrained=pretrained)
    torch.save(resnet18, f'{models_folder}/resnet18{suff}.pth')
    
    alexnet = models.alexnet(pretrained=pretrained)
    torch.save(alexnet, f'{models_folder}/alexnet{suff}.pth')

    vgg16 = models.vgg16(pretrained=pretrained)
    torch.save(vgg16, f'{models_folder}vgg16{suff}.pth')

    inception = models.inception_v3(pretrained=pretrained)
    torch.save(inception, f'{models_folder}/inception{suff}.pth')
    
    googlenet = models.googlenet(pretrained=pretrained)
    torch.save(googlenet, f'{models_folder}/googlenet{suff}.pth')

    mobilenet_v2 = models.mobilenet_v2(pretrained=pretrained)
    torch.save(mobilenet_v2, f'{models_folder}/mobilenet_v2{suff}.pth')

    mobilenet_v3_large = models.mobilenet_v3_large(pretrained=pretrained)
    torch.save(mobilenet_v3_large, f'{models_folder}mobilenet_v3_large{suff}.pth')

    mobilenet_v3_small = models.mobilenet_v3_small(pretrained=pretrained)
    torch.save(mobilenet_v3_small, f'{models_folder}/mobilenet_v3_small{suff}.pth')

    resnext50_32x4d = models.resnext50_32x4d(pretrained=pretrained)
    torch.save(resnext50_32x4d, f'{models_folder}/resnext50_32x4d{suff}.pth')

    wide_resnet50_2 = models.wide_resnet50_2(pretrained=pretrained)
    torch.save(wide_resnet50_2, f'{models_folder}/wide_resnet50_2{suff}.pth')

    mnasnet = models.mnasnet1_0(pretrained=pretrained)
    torch.save(mnasnet, f'{models_folder}/mnasnet{suff}.pth')

    efficientnet_b0 = models.efficientnet_b0(pretrained=pretrained)
    torch.save(efficientnet_b0, f'{models_folder}/efficientnet_b0{suff}.pth')

    efficientnet_b1 = models.efficientnet_b1(pretrained=pretrained)
    torch.save(efficientnet_b1, f'{models_folder}/efficientnet_b1{suff}.pth')

    efficientnet_b2 = models.efficientnet_b2(pretrained=pretrained)
    torch.save(efficientnet_b2, f'{models_folder}/efficientnet_b2{suff}.pth')

    efficientnet_b3 = models.efficientnet_b3(pretrained=pretrained)
    torch.save(efficientnet_b3, f'{models_folder}/efficientnet_b3{suff}.pth')

    efficientnet_b4 = models.efficientnet_b4(pretrained=pretrained)
    torch.save(efficientnet_b4, f'{models_folder}/efficientnet_b4{suff}.pth')

    efficientnet_b5 = models.efficientnet_b5(pretrained=pretrained)
    torch.save(efficientnet_b5, f'{models_folder}/efficientnet_b5{suff}.pth')

    efficientnet_b6 = models.efficientnet_b6(pretrained=pretrained)
    torch.save(efficientnet_b6, f'{models_folder}/efficientnet_b6{suff}.pth')

    efficientnet_b7 = models.efficientnet_b7(pretrained=pretrained)
    torch.save(efficientnet_b7, f'{models_folder}efficientnet_b7{suff}.pth')

    regnet_y_400mf = models.regnet_y_400mf(pretrained=pretrained)
    torch.save(regnet_y_400mf, f'{models_folder}/regnet_y_400mf{suff}.pth')

    regnet_y_800mf = models.regnet_y_800mf(pretrained=pretrained)
    torch.save(regnet_y_800mf, f'{models_folder}/regnet_y_800mf{suff}.pth')

    regnet_y_1_6gf = models.regnet_y_1_6gf(pretrained=pretrained)
    torch.save(regnet_y_1_6gf, f'{models_folder}/regnet_y_1_6gf{suff}.pth')

    regnet_y_3_2gf = models.regnet_y_3_2gf(pretrained=pretrained)
    torch.save(regnet_y_3_2gf, f'{models_folder}/regnet_y_3_2gf{suff}.pth')

    regnet_y_8gf = models.regnet_y_8gf(pretrained=pretrained)
    torch.save(regnet_y_8gf, f'{models_folder}/regnet_y_8gf{suff}.pth')

    regnet_y_16gf = models.regnet_y_16gf(pretrained=pretrained)
    torch.save(regnet_y_16gf, f'{models_folder}/regnet_y_16gf{suff}.pth')

    regnet_y_32gf = models.regnet_y_32gf(pretrained=pretrained)
    torch.save(regnet_y_32gf, f'{models_folder}/regnet_y_32gf{suff}.pth')

    regnet_x_400mf = models.regnet_x_400mf(pretrained=pretrained)
    torch.save(regnet_x_400mf, f'{models_folder}/regnet_x_400mf{suff}.pth')

    regnet_x_800mf = models.regnet_x_800mf(pretrained=pretrained)
    torch.save(regnet_x_800mf, f'{models_folder}/regnet_x_800mf{suff}.pth')

    regnet_x_1_6gf = models.regnet_x_1_6gf(pretrained=pretrained)
    torch.save(regnet_x_1_6gf, f'{models_folder}/regnet_x_1_6gf{suff}.pth')

    regnet_x_3_2gf = models.regnet_x_3_2gf(pretrained=pretrained)
    torch.save(regnet_x_3_2gf, f'{models_folder}/regnet_x_3_2gf{suff}.pth')

    regnet_x_8gf = models.regnet_x_8gf(pretrained=pretrained)
    torch.save(regnet_x_8gf, f'{models_folder}/regnet_x_8gf{suff}.pth')

    regnet_x_16gf = models.regnet_x_16gf(pretrained=pretrained)
    torch.save(regnet_x_16gf, f'{models_folder}/regnet_x_16gf{suff}.pth')

    regnet_x_32gf = models.regnet_x_32gf(pretrained=pretrained)
    torch.save(regnet_x_32gf, f'{models_folder}/regnet_x_32gf{suff}.pth')
    
    convnext_tiny = models.convnext_tiny(pretrained=pretrained)
    torch.save(convnext_tiny, f'{models_folder}/convnext_tiny{suff}.pth')

    convnext_small = models.convnext_small(pretrained=pretrained)
    torch.save(convnext_small, f'{models_folder}/convnext_small{suff}.pth')
