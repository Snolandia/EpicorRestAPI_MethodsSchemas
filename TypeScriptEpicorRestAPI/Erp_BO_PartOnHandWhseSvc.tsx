import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PartOnHandWhseSvc
// Description: Methods for retrieving on hand quanities
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartOnHandWhseSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartOnHandWhseSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetPartOnHandWhse
   Description: Get the Part quantity on hand records from the parameters.
   OperationID: GetPartOnHandWhse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartOnHandWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartOnHandWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartOnHandWhse(requestBody:GetPartOnHandWhse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartOnHandWhse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartOnHandWhseSvc/GetPartOnHandWhse", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPartOnHandWhse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_PartBinInfoRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Identifies the Part Number. It must be valid in the Part table.  */  
   PartNum:string,
      /**  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  */  
   WarehouseCode:string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   BinNum:string,
      /**  Indicates the desired minimum on-hand quantity.  */  
   MinimumQty:number,
      /**  Use to set a Maximum quantity limit that is desired to be on-hand.  */  
   MaximumQty:number,
      /**  Safety quantity is a "purchasing cushion" limit.  */  
   SafetyQty:number,
      /**  Uniquely indentifies the record.  */  
   KBCode:string,
      /**  Purchase order number  that the detail line item is linked to.  */  
   KBPONUM:number,
      /**  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   KBPOLine:number,
      /**  Kanban Warehouse  */  
   KBWarehouseCode:string,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   KBBinNum:string,
      /**  Site Identifier. This field cannot be blank.  */  
   KBPlant:string,
      /**  Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.  */  
   OnhandQty:number,
      /**  Indicates the desired minimum on-hand Kanban quantity.  */  
   KBQty:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   KBActionCode:string,
   KBActionDesc:string,
      /**  Maximum Quantity UOM  */  
   MaxQtyUOM:string,
      /**  Minimum Quantity UOM  */  
   MinQtyUOM:string,
      /**  Filled in by BO, not phiscally in database.  */  
   Plant:string,
   PlantOwner:string,
      /**  Safety Quantity UOM  */  
   SafetyQtyUOM:string,
   BitFlag:number,
   BinNumDescription:string,
   BinNumNonNettable:boolean,
   KBBinNumDescription:string,
   KBCodeKBDescription:string,
   KBCodeKBActionCode:string,
   KBPlantName:string,
   KBWarehouseCodeDescription:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartOnHandBinRow{
   Company:string,
   PartNum:string,
   Plant:string,
   WarehouseCode:string,
   BinNum:string,
   LotNum:string,
   DimCode:string,
   QuantityOnHand:number,
   NonNettable:boolean,
   BinDescription:string,
   UnitOfMeasure:string,
   IsPrimaryBin:string,
   SeqNum:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartOnHandWhseRow{
   Company:string,
   PartNum:string,
   Plant:string,
   WarehouseCode:string,
   WarehouseDesc:string,
   PrimaryBinNum:string,
   AllocQty:number,
   IUM:string,
   QuantityOnHand:number,
   CountedDate:string,
   IsPrimaryWarehouse:string,
   MultipleUOMs:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartOnHandWhseTableset{
   PartOnHandWhse:Erp_Tablesets_PartOnHandWhseRow[],
   PartOnHandBin:Erp_Tablesets_PartOnHandBinRow[],
   PartBinInfo:Erp_Tablesets_PartBinInfoRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param cPartNum
      @param cPlant
   */  
export interface GetPartOnHandWhse_input{
      /**  The Part Number  */  
   cPartNum:string,
      /**  The plant  */  
   cPlant:string,
}

export interface GetPartOnHandWhse_output{
   returnObj:Erp_Tablesets_PartOnHandWhseTableset[],
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

