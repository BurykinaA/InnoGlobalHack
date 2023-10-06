from sklearn.metrics import confusion_matrix, precision_score, recall_score
from tqdm import tqdm
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
from sklearn.metrics import f1_score

mtcnn_model = MTCNN().eval().cpu()  # MTCNN на CPU
resnet_model = InceptionResnetV1(pretrained="vggface2").eval().to(device)


def test(model, device, valid):
    model.eval()
    correct = 0
    all_labels = []
    all_predictions = []
    mistakes = []

    for i in tqdm(range(len(valid))):
        X = torch.tensor(valid[i][0]).unsqueeze(0).to(device).float()
        y = torch.tensor(valid[i][1]).unsqueeze(0).to(device).long()

        with torch.no_grad():
            outputs = model(X, mtcnn_model, resnet_model)
            _, predicted = torch.max(outputs.data, 1)
            correct += (predicted == y).sum().item()
            if predicted != y:
                mistakes.append(i)

            # Сохраняем метки и прогнозы для вычисления F1-оценки
            all_labels.extend([y.cpu().item()])
            all_predictions.extend(predicted.cpu().numpy())

    val_accuracy = 100.0 * correct / len(all_labels)

    # Вычисляем F1-оценку
    f1 = f1_score(all_labels, all_predictions, average="weighted")

    # Вычисляем TP, TN, FP и FN
    tn, fp, fn, tp = confusion_matrix(all_labels, all_predictions).ravel()

    # Вычисляем точность и полноту
    precision = precision_score(all_labels, all_predictions)
    recall = recall_score(all_labels, all_predictions)

    for i in mistakes:
        valid.show_img(i)

    return val_accuracy, f1, tp, tn, fp, fn, precision, recall
