<script>
import { Doughnut } from "vue-chartjs";

export default {
  extends: Doughnut,
  data: () => ({
    chartdata: {
      labels: ["비숑", "푸들", "시바"],
      datasets: [
        {
          backgroundColor: [
            "rgba(87,130,187,1)",
            "rgba(100,215,214,1)",
            "rgba(196,175,240,1)",
          ],
          data: [13, 26, 80],
          borderAlign: "center",
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  }),
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>

<style>
.chartjs-render-monitor {
  height: 200px;
  text-align: center;
}
</style>