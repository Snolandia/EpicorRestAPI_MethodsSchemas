import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMFSCallhdSvc
# Description: Business Object to handle: Count, Get, Ack, and GetAll of FSCallhd
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AckFSCallhd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AckFSCallhd
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountFSCallhd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountFSCallhd
   Description: Returns the count of existing IntQueOut records along with the count of updated FSCallhds in the database that IntQueOut records have not yet been created for
   OperationID: CountFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllFSCallhd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllFSCallhd
   Description: Generates IntQueOut and IMFSCallhd rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFSCallhd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFSCallhd
   Description: Generates IntQueOut and IMFSCallhd rows since the last time this was called and then returns these along with any existing
   OperationID: GetFSCallhd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFSCallhd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFSCallhd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSCallhdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AckFSCallhd_input:
   """ Required : 
   ts
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.ts:list[Erp_Tablesets_IMFSCallhdTableset] = obj["ts"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class AckFSCallhd_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class CountFSCallhd_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class CountFSCallhd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMFSCallDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CallLine:int = obj["CallLine"]
      """  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the part being repaired.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.CallQty:int = obj["CallQty"]
      """  TotalCall Quantity for the line item.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number if this item is under a contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This is the contract line the relates to the item on the service call.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  """  
      self.ProbReasonCode:str = obj["ProbReasonCode"]
      """  Problem reason code from the reason master table. type problem.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.TotLabor:int = obj["TotLabor"]
      """  total Labor Amount.  """  
      self.DocTotLabor:int = obj["DocTotLabor"]
      """  total Labor Amount. In customers currency  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  total Billable Labor Amount.  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  total Billable Labor Amount. In Customers currency.  """  
      self.TotMaterial:int = obj["TotMaterial"]
      """  total Material Amount.  """  
      self.DocTotMaterial:int = obj["DocTotMaterial"]
      """  total Material Amount. In Customers currency  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  total Billable Material Amount.  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  total Billable Material Amount. In Customers Currency.  """  
      self.TotMisc:int = obj["TotMisc"]
      """  total Misc. Amount.  """  
      self.DocTotMisc:int = obj["DocTotMisc"]
      """  total Misc. Amount. In customers currency.  """  
      self.TotBillableMisc:int = obj["TotBillableMisc"]
      """  total Billable Misc. Amount.  """  
      self.DocTotBillableMisc:int = obj["DocTotBillableMisc"]
      """  total Billable Misc. Amount. In customer's currency.  """  
      self.TotMaterialCost:int = obj["TotMaterialCost"]
      """  total Material Cost.  """  
      self.TotMiscCost:int = obj["TotMiscCost"]
      """  total Misc. Cost.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSCallDt record. Can be blank.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotSubCont:int = obj["TotSubCont"]
      """  Total Subcontract Amount.  """  
      self.DocTotSubCont:int = obj["DocTotSubCont"]
      """  total Subcontract Amount. In customers currency  """  
      self.TotBillSubCont:int = obj["TotBillSubCont"]
      """  total Billable Subcontract Amount.  """  
      self.DocTotBillSubCont:int = obj["DocTotBillSubCont"]
      """  total Billable Subcontract Amount. In Customers currency.  """  
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  total Estimated Labor Amount.  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  total estimated Labor Amount. In customers currency  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  total Estimated Material Amount.  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  total Estimated Material Amount. In Customers currency  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  total Estimated Misc. Amount.  Future Use.  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  total Est. Misc. Amount. In customers currency. Future use  """  
      self.TotEstSubCont:int = obj["TotEstSubCont"]
      """  Total estimated Subcontract Amount.  """  
      self.DocTotEstSubCont:int = obj["DocTotEstSubCont"]
      """  total Estimated Subcontract Amount. In customers currency  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1TotBillableMisc:int = obj["Rpt1TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillableMisc:int = obj["Rpt2TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillableMisc:int = obj["Rpt3TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillSubCont:int = obj["Rpt1TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillSubCont:int = obj["Rpt2TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillSubCont:int = obj["Rpt3TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstSubCont:int = obj["Rpt1TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstSubCont:int = obj["Rpt2TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstSubCont:int = obj["Rpt3TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotLabor:int = obj["Rpt1TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotLabor:int = obj["Rpt2TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotLabor:int = obj["Rpt3TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMaterial:int = obj["Rpt1TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMaterial:int = obj["Rpt2TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMaterial:int = obj["Rpt3TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMisc:int = obj["Rpt1TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMisc:int = obj["Rpt2TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMisc:int = obj["Rpt3TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotSubCont:int = obj["Rpt1TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotSubCont:int = obj["Rpt2TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotSubCont:int = obj["Rpt3TotSubCont"]
      """  Reporting currency value of this field  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  IssueTopicID1  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  IssueTopicID2  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  IssueTopicID3  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  IssueTopicID4  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  IssueTopicID5  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  IssueTopicID6  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  IssueTopicID7  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  IssueTopicID8  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  IssueTopicID9  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  IssueTopicID10  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  IssueTopics  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  ResTopicID1  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  ResTopicID2  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  ResTopicID3  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  ResTopicID4  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  ResTopicID5  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  ResTopicID6  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  ResTopicID7  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  ResTopicID8  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  ResTopicID9  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  ResTopicID10  """  
      self.ResTopics:str = obj["ResTopics"]
      """  ResTopics  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates the invoice processing has been done for this call line.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call line can be invoiced.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Key from related IntQueInOut  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMFSCallhdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Customer Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  defaults to TODAY  """  
      self.EntryTime:int = obj["EntryTime"]
      """  Time in second past midnight  """  
      self.RequestDate:str = obj["RequestDate"]
      """  The date that the service is requested for.  """  
      self.RequestTime:int = obj["RequestTime"]
      """  Time in second past midnight  """  
      self.SchedDate:str = obj["SchedDate"]
      """  The date that the service is scheduled for.  """  
      self.SchedTime:int = obj["SchedTime"]
      """  Time in second past midnight  """  
      self.ActualDate:str = obj["ActualDate"]
      """  The date that the service was performed on.  """  
      self.ActualTime:int = obj["ActualTime"]
      """  Time in second past midnight  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Contains comments about the overall Call. These will be printed on the Service Call invoice.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this Call.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call is closed and can be invoiced.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicated the invoice processing has been done for this call.  """  
      self.VoidCall:bool = obj["VoidCall"]
      """  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  """  
      self.CallPriority:str = obj["CallPriority"]
      """  Can have 3 values High, normal and, Low  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Service call entry edit reports. The intent is for users to be able to select Contract that they have entered for hard copy edit.
On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  """  
      self.LaborComplete:bool = obj["LaborComplete"]
      """   Set from labor entry.  Indicates that all labor has been entered for this call.  if this flag and the Material complete flag are set then the
opencall field will be set to FALSE and the READY TO INVOICE flag will be set o TRUE.  """  
      self.MaterialComplete:bool = obj["MaterialComplete"]
      """  Set from Issue materials.  Indicates that all material have been issued for this call.  if this flag and the Labor complete flag are set then the opencall field will be set to FALSE and the READY TO INVOICE flag will be set to TRUE.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Duration:int = obj["Duration"]
      """  The estimated duration of the service call in days.  """  
      self.CLCallNum:str = obj["CLCallNum"]
      """  The Clientele call number that is related to this call.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this service call.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping country number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PONum:str = obj["PONum"]
      """  PONum  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the service call has to be synchronized with Epicor FSA application.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.CustID:str = obj["CustID"]
      self.CallDescription:str = obj["CallDescription"]
      self.IntQueID:int = obj["IntQueID"]
      """  Key from related IntQueInOut  """  
      self.ShipToName:str = obj["ShipToName"]
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMFSCallhdTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMFSCallDt:list[Erp_Tablesets_IMFSCallDtRow] = obj["IMFSCallDt"]
      self.IMFSCallhd:list[Erp_Tablesets_IMFSCallhdRow] = obj["IMFSCallhd"]
      self.IMFsTech:list[Erp_Tablesets_IMFsTechRow] = obj["IMFsTech"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMFsTechRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  The call number that the technician is assigned to.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Part of the unique for this table.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.Name:str = obj["Name"]
      """  the name of the employee assigned to the service call.  """  
      self.OpenCall:bool = obj["OpenCall"]
      """  Indicate that the call is open.  Not directly maintainable.  This is a mirror image of FSCallHd.OpenCall and is maintained by the WRITE trigger of FSCallHd.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Key from related IntQueInOut  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInOutRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique key from IntQueIn or IntQueOut  """  
      self.Action:str = obj["Action"]
      """  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  """  
      self.IncomingOutgoing:str = obj["IncomingOutgoing"]
      """  "I" for incoming or "O" for outgoing  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAllFSCallhd_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetAllFSCallhd_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMFSCallhdTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetFSCallhd_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetFSCallhd_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMFSCallhdTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

