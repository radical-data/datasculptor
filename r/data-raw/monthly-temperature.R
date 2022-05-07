monthly <- readr::read_csv("data-raw/monthly-temperature.csv")

monthly <- monthly |>
  janitor::clean_names() |>
  filter(source == "GISTEMP") |>
  mutate(month = lubridate::month(date),
         year = lubridate::year(date)) |>
  rename(temperature_anomaly = mean) |>
  select(year, month, temperature_anomaly)

monthly <- monthly |>
  mutate(year = year - mean(year),
         month = month - mean(month))

write_csv(monthly, file = here::here("data/monthly.csv"), col_names = FALSE)
usethis::use_data(monthly, overwrite = TRUE)
