CREATE INDEX "ОЦЕНКА_ИНДЕКС" ON "Н_ВЕДОМОСТИ" using hash("ОЦЕНКА");
CREATE INDEX "КОД_ИНДЕКС" ON "Н_ОЦЕНКИ" using btree("КОД");
CREATE INDEX "ЧЛВК_ИД_ИНДЕКС" ON "Н_ВЕДОМОСТИ" using btree("ЧЛВК_ИД");