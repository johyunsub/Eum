<script>
import { Doughnut } from "vue-chartjs";
import { mapState } from "vuex";

export default {
  extends: Doughnut,
  computed: {
    ...mapState(["chartInfo", "dogListIdx"]),
  },
  data: () => ({
    chartdata: {
      labels: ["", "", ""],
      datasets: [
        {
          backgroundColor: [
            "rgba(253,146,145,1)",
            "rgba(245,252,158)",
            "rgba(158,252,180,1)",
          ],
          data: [0, 0, 0],
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
  created() {
    const idx = this.dogListIdx * 3;
    this.chartdata.labels[0] = this.chartInfo[idx].predictedBreed;
    this.chartdata.labels[1] = this.chartInfo[idx + 1].predictedBreed;
    this.chartdata.labels[2] = this.chartInfo[idx + 2].predictedBreed;
    this.chartdata.datasets[0].data[0] =
      Math.floor(this.chartInfo[idx].percent * 100) / 100;
    this.chartdata.datasets[0].data[1] =
      Math.floor(this.chartInfo[idx + 1].percent * 100) / 100;
    this.chartdata.datasets[0].data[2] =
      Math.floor(this.chartInfo[idx + 2].percent * 100) / 100;
  },
};
</script>

<style>
.chartjs-render-monitor {
  height: 200px;
  text-align: center;
  font-size: 30px;
}
</style>