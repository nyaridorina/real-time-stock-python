import plotly.express as px
import pandas as pd

# Create a dictionary with the provided meditations list
data = {
    'Technique Focus': ['Mindfulness meditation', 'Transcendental meditation', 'Loving-kindness meditation (Metta)', 'Vipassana meditation', 'Zen meditation (Zazen)', 'Yoga nidra', 'Guided visualization meditation', 'Body scan meditation', 'Chakra meditation', 'Breath awareness meditation (Anapanasati)', 'Mantra meditation', 'Walking meditation (Kinhin)', 'Tonglen meditation', 'Sound meditation (Nada yoga)', 'Kundalini meditation', 'Taoist meditation', 'Qigong meditation', 'Reiki meditation', 'Christian meditation (Contemplative prayer)', 'Sufi meditation', 'Shamanic journeying', 'Dynamic meditation (Osho meditation)', 'Biofeedback meditation', 'Mindfulness-Based Stress Reduction (MBSR)'],
    'Origin or Tradition': ['Mindfulness', 'Concentration', 'Compassion', 'Insight', 'Concentration, Mindfulness', 'Relaxation', 'Visualization', 'Mindfulness', 'Concentration, Energy Work', 'Concentration', 'Concentration', 'Mindfulness', 'Compassion', 'Concentration', 'Energy Work', 'Various (Concentration, Energy Work)', 'Movement, Energy Work', 'Energy Work', 'Contemplation', 'Various (Concentration, Devotion)', 'Visualization', 'Movement, Catharsis', 'Relaxation, Self-regulation', 'Mindfulness'],
    'Activity Level': ['Passive', 'Passive', 'Passive', 'Passive', 'Passive', 'Passive', 'Passive', 'Passive', 'Passive', 'Passive', 'Passive', 'Active', 'Passive', 'Passive', 'Active/Passive', 'Passive', 'Active', 'Passive', 'Passive', 'Passive/Active', 'Passive/Active', 'Active', 'Passive', 'Passive'],
    'Intended Benefit': ['Awareness, presence', 'Stress relief, self-development', 'Cultivate compassion', 'Self-awareness, insight', 'Enlightenment, presence', 'Deep relaxation, stress relief', 'Relaxation, mental rehearsal', 'Body awareness, relaxation', 'Energy balance, healing', 'Concentration, mindfulness', 'Focus, tranquility', 'Mindfulness in motion', 'Developing empathy, compassion', 'Concentration, peace', 'Awakening energy, consciousness', 'Harmony, balance', 'Health, vitality', 'Healing, balance', 'Spiritual connection, contemplation', 'Spiritual unity, love', 'Healing, guidance', 'Release, awareness', 'Stress relief, self-regulation', 'Stress reduction, health'],
    'Goal or Purpose': ['Spiritual, Secular', 'Spiritual', 'Spiritual', 'Spiritual', 'Spiritual', 'Spiritual, Secular', 'Secular', 'Secular', 'Spiritual', 'Spiritual', 'Spiritual', 'Spiritual', 'Spiritual', 'Spiritual', 'Spiritual', 'Spiritual', 'Spiritual', 'Secular', 'Spiritual', 'Spiritual', 'Spiritual', 'Spiritual', 'Secular', 'Secular'],
    'Guidance Level': ['Guided or Unguided', 'Guided', 'Guided', 'Guided or Unguided', 'Unguided, sometimes guided', 'Guided', 'Guided', 'Guided or Unguided', 'Guided or Unguided', 'Guided or Unguided', 'Guided or Unguided', 'Unguided', 'Guided or Unguided', 'Unguided, sometimes guided', 'Guided or Unguided', 'Guided or Unguided', 'Guided or Unguided', 'Guided or Unguided', 'Guided or Unguided', 'Guided or Unguided', 'Guided', 'Guided', 'Guided with equipment', 'Guided']
}

# Create a DataFrame with the provided meditations list
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Create a scatter plot using the meditations data
fig = px.scatter(df, x='Technique Focus', y='Intended Benefit', color='Origin or Tradition', title='Meditation Techniques and Benefits')

# Show the plot
fig.show()