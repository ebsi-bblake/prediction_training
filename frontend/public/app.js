import m from 'mithril';

const Predict = {
  feature1: 0,
  feature2: 0,
  feature3: 0,
  feature4: 0,
  feature5: 0,
  feature6: 0,
  feature7: 0,
  result: null,
  predict: () => {
    m.request({
      method: "POST",
      url: "/api/predict",
      body: {
        feature1: Predict.feature1,
        feature2: Predict.feature2,
        feature3: Predict.feature3,
        feature4: Predict.feature4,
        feature5: Predict.feature5,
        feature6: Predict.feature6,
        feature7: Predict.feature7,
      }
    })
      .then(result => {
        Predict.result = result.predicted_value;
      });
  },
  view: () => {
    return m("div", [
      m("input[type=number]", { oninput: e => Predict.feature1 = e.target.value, placeholder: "Feature 1" }),
      m("input[type=number]", { oninput: e => Predict.feature2 = e.target.value, placeholder: "Feature 2" }),
      m("input[type=number]", { oninput: e => Predict.feature3 = e.target.value, placeholder: "Feature 3" }),
      m("input[type=number]", { oninput: e => Predict.feature4 = e.target.value, placeholder: "Feature 4" }),
      m("input[type=number]", { oninput: e => Predict.feature5 = e.target.value, placeholder: "Feature 5" }),
      m("input[type=number]", { oninput: e => Predict.feature6 = e.target.value, placeholder: "Feature 6" }),
      m("input[type=number]", { oninput: e => Predict.feature7 = e.target.value, placeholder: "Feature 7" }),
      m("button", { onclick: Predict.predict }, "Predict"),
      Predict.result !== null ? m("div", `Predicted Value: ${Predict.result}`) : null
    ]);
  }
};

m.mount(document.body, Predict);
