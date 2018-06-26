python3 train.py \
  --how_many_training_steps=2000 \
  --model_dir=inception \
  --output_graph=logs/trained_graph.pb \
  --output_labels=logs/trained_labels.txt \
  --image_dir=./dataset
#  --bottleneck_dir=logs/bottlenecks \
#  --summaries_dir=logs/training_summaries/basic \