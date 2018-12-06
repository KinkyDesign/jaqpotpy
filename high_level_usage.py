from jaqpotpy import Jaqpot
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import matplotlib
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import SVR
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from base64 import b64encode, b64decode
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
import tempfile
import base64
from subprocess import call
import pydotplus


# jaqp = jap.Jaqpot("https://api.jaqpot.org/jaqpot/services/")

jaqpot = Jaqpot("http://localhost:8080/jaqpot/services/")
jaqpot.request_key("pantelispanka", "kapan1")

# jaqp.request_key_safe()

# jaqpot.my_info()
# algos = jaqpot.get_algorithms()

# print(algos)

# algos_classes = jaqp.get_algorithms_classes()
# for algo in algos_classes:
#     print(algo.meta)

# df = pd.read_csv('/Users/pantelispanka/Desktop/gdp-countries.csv')
# print(df.dtypes)

df2 = pd.read_csv('/Users/pantelispanka/Desktop/train.csv')
# print(df2.dtypes)
# jaqpot.upload_dataset(df=df, id='country')


# jaqpot.upload_dataset(df=df2, id='PassengerId')

# lm = LinearRegression()
#
# y = df['GDP']
# X = df[['LFG', 'EQP', 'NEQ', 'GAP']]
#
# model = lm.fit(X=X, y=y)

# pred = model.predict(X)


# jaqpot.deploy_linear_model(model, X, y, title="Sklearn linear", description="First pretrained from python",
#                   algorithm="linear_model")


print(list(df2))

X2 = df2[['Pclass',  'SibSp', 'Parch', 'Fare']]
y2 = df2['Survived']

clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(X2, y2)

print(clf.predict(X2))

jaqpot.deploy_linear_model(clf, X2, y2, title="Sklearn logistic", description="Logistic pretrained from python",
                  algorithm="logistic regression")


# estimator = DecisionTreeClassifier(random_state=0).fit(X2, y2)

# jaqpot.deploy_tree(estimator, X2, y2, title="Sklearn tree", description="Decision tree pretrained from python",
#                   algorithm="Decision tree")


# ensemble = BaggingClassifier().fit(X2, y2)


# jaqpot.deploy_ensemble(ensemble, X2, y2, title="Sklearn ensemble", description="Bagging classifier pretrained from python",
#                   algorithm="BaggingClassifier")


# svr = SVR().fit(X2, y2)

# jaqpot.deploy_svm(ensemble, X2, y2, title="Sklearn svm", description="Svm classifier pretrained from python",
#                   algorithm="Svr")

# dot_data = StringIO()
# export_graphviz(estimator, out_file=dot_data,
#                 filled=True, rounded=True,
#                 special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# print(graph.create_png())



# print(tree.predict(X2))
# treei
# print(tree.tree_.node_count)


# n_nodes = estimator.tree_.node_count
# children_left = estimator.tree_.children_left
# children_right = estimator.tree_.children_right
# feature = estimator.tree_.feature
# threshold = estimator.tree_.threshold
#
#
# # The tree structure can be traversed to compute various properties such
# # as the depth of each node and whether or not it is a leaf.
# node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
# is_leaves = np.zeros(shape=n_nodes, dtype=bool)
# stack = [(0, -1)]  # seed is the root node id and its parent depth
# while len(stack) > 0:
#     node_id, parent_depth = stack.pop()
#     node_depth[node_id] = parent_depth + 1
#
#     # If we have a test node
#     if (children_left[node_id] != children_right[node_id]):
#         stack.append((children_left[node_id], parent_depth + 1))
#         stack.append((children_right[node_id], parent_depth + 1))
#     else:
#         is_leaves[node_id] = True
#
# print("The binary tree structure has %s nodes and has "
#       "the following tree structure:"
#       % n_nodes)
# for i in range(n_nodes):
#     if is_leaves[i]:
#         print("%snode=%s leaf node." % (node_depth[i] * "\t", i))
#     else:
#         print("%snode=%s test node: go to node %s if X[:, %s] <= %s else to "
#               "node %s."
#               % (node_depth[i] * "\t",
#                  i,
#                  children_left[i],
#                  feature[i],
#                  threshold[i],
#                  children_right[i],
#                  ))
# print()

# First let's retrieve the decision path of each sample. The decision_path
# method allows to retrieve the node indicator functions. A non zero element of
# indicator matrix at the position (i, j) indicates that the sample i goes
# through the node j.

# node_indicator = estimator.decision_path(X2)

# Similarly, we can also have the leaves ids reached by each sample.

# leave_id = estimator.apply(X2)

# Now, it's possible to get the tests that were used to predict a sample or
# a group of samples. First, let's make it for the sample.

# sample_id = 0
# node_index = node_indicator.indices[node_indicator.indptr[sample_id]:
#                                     node_indicator.indptr[sample_id + 1]]

# print('Rules used to predict sample %s: ' % sample_id)
# for node_id in node_index:
#     if leave_id[sample_id] == node_id:
#         continue
#
#     if (X2[sample_id, feature[node_id]] <= threshold[node_id]):
#         threshold_sign = "<="
#     else:
#         threshold_sign = ">"
#
#     print("decision id node %s : (X_test[%s, %s] (= %s) %s %s)"
#           % (node_id,
#              sample_id,
#              feature[node_id],
#              X2[sample_id, feature[node_id]],
#              threshold_sign,
#              threshold[node_id]))
#
# # For a group of samples, we have the following common node.
# sample_ids = [0, 1]
# common_nodes = (node_indicator.toarray()[sample_ids].sum(axis=0) ==
#                 len(sample_ids))
#
# common_node_id = np.arange(n_nodes)[common_nodes]
#
# print("\nThe following samples %s share the node %s in the tree"
#       % (sample_ids, common_node_id))
# print("It is %s %% of all nodes." % (100 * len(common_node_id) / n_nodes,))
# res_plot = sns.residplot(y, pred, lowess=True, color="g")
# plt.show()

# plt.scatter(X, y,  color='black')
# plt.plot(X, model.predict(X), color='blue', linewidth=1)
# plt.xticks(())
# plt.yticks(())
# plt.show()