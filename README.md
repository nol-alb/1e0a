# '1e0a': A Computational Approach to Rhythm Training
We present a computational assessment system that promotes the learning of basic rhythmic patterns. The system is capable of generating multiple rhythmic patterns with increasing complexity within various cycle lengths. For a generated rhythm pattern the performance assessment of the learner is carried out through the statistical deviations calculated from the onset detection and temporal assessment of a learner's performance. This is compared with the generated pattern, and their performance accuracy forms the feedback to the learner. The system proceeds to generate a new pattern of increased complexity when performance assessment results are within certain error bounds. The system thus mimics a learner-teacher relationship as the learner progresses in their feedback-based learning. The choice of progression within a cycle for each pattern is determined by a predefined complexity metric. This metric is based on a coded element model for the perceptual processing of sequential stimuli. The model earlier proposed for a sequence of tones and non-tones, is now used for onsets and silences. This system is developed into a web-based application and provides accessibility for learning purposes. Analysis of the performance assessments shows that the complexity metric is indicative of the perceptual processing of rhythm patterns and can be used for rhythm learning. 

### Methodology
![alt text](https://github.com/nol-alb/1e0a/blob/main/flow/flow.png)

 This system consists of two distinct blocks:
 (1) The rhythm pattern generator with the complexity metric\
 (2) the performance assessment of the learner input with feedback.
 
 The Web Application can be accessed here:https://1e0a.noelalben.com
