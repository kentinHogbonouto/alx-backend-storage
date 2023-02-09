-- Trigger executed upon inserting into
-- the orders table
DROP TRIGGER IF EXISTS update_item_count;
CREATE TRIGGER update_item_count AFTER INSERT on orders
FOR EACH ROW
UPDATE items
SET items.quantity = items.quantity - NEW.number
WHERE items.name = NEW.item_name
