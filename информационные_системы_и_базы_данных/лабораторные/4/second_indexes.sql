CREATE INDEX "ЛЮДИ_ИД_ИНДЕКС" ON "Н_ЛЮДИ" using hash("ИД");
CREATE INDEX "ВЕДОМОСТИ_ЧЛВК_ИД_ИНДЕКС" ON "Н_ВЕДОМОСТИ" using hash("ЧЛВК_ИД");
CREATE INDEX "СЕССИЯ_ЧЛВК_ИД_ИНДЕКС" ON "Н_СЕССИЯ" using hash("ЧЛВК_ИД");
CREATE INDEX "ИМЯ_ИНДЕКС" ON "Н_ЛЮДИ" using btree("ИМЯ");
CREATE INDEX "ВЕДОМОСТИ_ИД_ИНДЕКС" ON "Н_ВЕДОМОСТИ" using btree("ИД");