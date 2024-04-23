import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MeterReadSvc
# Description: Created for Equipment Meter Reading Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MeterReads(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MeterReads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MeterReads
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MeterReadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads",headers=creds) as resp:
           return await resp.json()

async def post_MeterReads(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MeterReads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MeterReadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MeterReadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MeterReads_Company_EquipID(Company, EquipID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MeterRead item
   Description: Calls GetByID to retrieve the MeterRead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MeterRead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MeterReadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads(" + Company + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MeterReads_Company_EquipID(Company, EquipID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MeterRead for the service
   Description: Calls UpdateExt to update MeterRead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MeterRead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MeterReadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads(" + Company + "," + EquipID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MeterReads_Company_EquipID(Company, EquipID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MeterRead item
   Description: Call UpdateExt to delete MeterRead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MeterRead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads(" + Company + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MeterReadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMeterRead, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMeterRead=" + whereClauseMeterRead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(equipID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "equipID=" + equipID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMeterRead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMeterRead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMeterRead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMeterRead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMeterRead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MeterReadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MeterReadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MeterReadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MeterReadRow] = obj["value"]
      pass

class Erp_Tablesets_MeterReadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Plant:str = obj["Plant"]
      """  Site in which the equipment is currently located.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.StatusID:str = obj["StatusID"]
      """  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  """  
      self.OEM:str = obj["OEM"]
      """  OEM Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Serial Number of equipment  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.Model:str = obj["Model"]
      """  Model Number  """  
      self.InServiceDate:str = obj["InServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.WarrantyExpDate:str = obj["WarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.TypeID:str = obj["TypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SellingVendorNum:int = obj["SellingVendorNum"]
      """  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.SellingPurPoint:str = obj["SellingPurPoint"]
      """  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.ServiceVendorNum:int = obj["ServiceVendorNum"]
      """  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.ServicePurPoint:str = obj["ServicePurPoint"]
      """  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Foreign Component key to the FAsset table.  """  
      self.Comments:str = obj["Comments"]
      """  Comments about the Equipment.  """  
      self.Specs:str = obj["Specs"]
      """  Allows entry of freeform equipment specifications.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  """  
      self.ReadingComment:str = obj["ReadingComment"]
      """  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  """  
      self.LocID:str = obj["LocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.ParentEquipID:str = obj["ParentEquipID"]
      """  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  """  
      self.LaborMeterOpt:str = obj["LaborMeterOpt"]
      """   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  """  
      self.ReadingDate:str = obj["ReadingDate"]
      """  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  """  
      self.ReadingTime:int = obj["ReadingTime"]
      """  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.AvgDailyUsage:int = obj["AvgDailyUsage"]
      self.GlobalEquip:bool = obj["GlobalEquip"]
      """  Marks this Equip as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NewMeter:int = obj["NewMeter"]
      """  External field used to enter a NEW meter reading valule.  When saved, it will update Equip.CurrentMeter, and them be set to zero for the next transaction.  """  
      self.NewReadingComment:str = obj["NewReadingComment"]
      """  Used to enter a comment related to the NEW meter reading.  When saved, this value updates current reading comment (Equip.ReadingComment) and is then blanked out.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MeterReadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Plant:str = obj["Plant"]
      """  Site in which the equipment is currently located.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.StatusID:str = obj["StatusID"]
      """  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  """  
      self.OEM:str = obj["OEM"]
      """  OEM Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Serial Number of equipment  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.Model:str = obj["Model"]
      """  Model Number  """  
      self.InServiceDate:str = obj["InServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.WarrantyExpDate:str = obj["WarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.TypeID:str = obj["TypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SellingVendorNum:int = obj["SellingVendorNum"]
      """  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.SellingPurPoint:str = obj["SellingPurPoint"]
      """  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.ServiceVendorNum:int = obj["ServiceVendorNum"]
      """  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.ServicePurPoint:str = obj["ServicePurPoint"]
      """  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Foreign Component key to the FAsset table.  """  
      self.Comments:str = obj["Comments"]
      """  Comments about the Equipment.  """  
      self.Specs:str = obj["Specs"]
      """  Allows entry of freeform equipment specifications.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  """  
      self.ReadingComment:str = obj["ReadingComment"]
      """  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  """  
      self.LocID:str = obj["LocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.ParentEquipID:str = obj["ParentEquipID"]
      """  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  """  
      self.LaborMeterOpt:str = obj["LaborMeterOpt"]
      """   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  """  
      self.ReadingDate:str = obj["ReadingDate"]
      """  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  """  
      self.ReadingTime:int = obj["ReadingTime"]
      """  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.AvgDailyUsage:int = obj["AvgDailyUsage"]
      self.GlobalEquip:bool = obj["GlobalEquip"]
      """  Marks this Equip as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NewMeter:int = obj["NewMeter"]
      """  External field used to enter a NEW meter reading valule.  When saved, it will update Equip.CurrentMeter, and them be set to zero for the next transaction.  """  
      self.NewReadingComment:str = obj["NewReadingComment"]
      """  Used to enter a comment related to the NEW meter reading.  When saved, this value updates current reading comment (Equip.ReadingComment) and is then blanked out.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   equipID
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MeterReadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Plant:str = obj["Plant"]
      """  Site in which the equipment is currently located.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.StatusID:str = obj["StatusID"]
      """  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  """  
      self.OEM:str = obj["OEM"]
      """  OEM Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Serial Number of equipment  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.Model:str = obj["Model"]
      """  Model Number  """  
      self.InServiceDate:str = obj["InServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.WarrantyExpDate:str = obj["WarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.TypeID:str = obj["TypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SellingVendorNum:int = obj["SellingVendorNum"]
      """  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.SellingPurPoint:str = obj["SellingPurPoint"]
      """  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.ServiceVendorNum:int = obj["ServiceVendorNum"]
      """  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.ServicePurPoint:str = obj["ServicePurPoint"]
      """  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Foreign Component key to the FAsset table.  """  
      self.Comments:str = obj["Comments"]
      """  Comments about the Equipment.  """  
      self.Specs:str = obj["Specs"]
      """  Allows entry of freeform equipment specifications.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  """  
      self.ReadingComment:str = obj["ReadingComment"]
      """  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  """  
      self.LocID:str = obj["LocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.ParentEquipID:str = obj["ParentEquipID"]
      """  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  """  
      self.LaborMeterOpt:str = obj["LaborMeterOpt"]
      """   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  """  
      self.ReadingDate:str = obj["ReadingDate"]
      """  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  """  
      self.ReadingTime:int = obj["ReadingTime"]
      """  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.AvgDailyUsage:int = obj["AvgDailyUsage"]
      self.GlobalEquip:bool = obj["GlobalEquip"]
      """  Marks this Equip as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NewMeter:int = obj["NewMeter"]
      """  External field used to enter a NEW meter reading valule.  When saved, it will update Equip.CurrentMeter, and them be set to zero for the next transaction.  """  
      self.NewReadingComment:str = obj["NewReadingComment"]
      """  Used to enter a comment related to the NEW meter reading.  When saved, this value updates current reading comment (Equip.ReadingComment) and is then blanked out.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MeterReadListTableset:
   def __init__(self, obj):
      self.MeterReadList:list[Erp_Tablesets_MeterReadListRow] = obj["MeterReadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MeterReadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Plant:str = obj["Plant"]
      """  Site in which the equipment is currently located.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.StatusID:str = obj["StatusID"]
      """  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  """  
      self.OEM:str = obj["OEM"]
      """  OEM Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Serial Number of equipment  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.Model:str = obj["Model"]
      """  Model Number  """  
      self.InServiceDate:str = obj["InServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.WarrantyExpDate:str = obj["WarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.TypeID:str = obj["TypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SellingVendorNum:int = obj["SellingVendorNum"]
      """  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.SellingPurPoint:str = obj["SellingPurPoint"]
      """  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.ServiceVendorNum:int = obj["ServiceVendorNum"]
      """  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.ServicePurPoint:str = obj["ServicePurPoint"]
      """  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Foreign Component key to the FAsset table.  """  
      self.Comments:str = obj["Comments"]
      """  Comments about the Equipment.  """  
      self.Specs:str = obj["Specs"]
      """  Allows entry of freeform equipment specifications.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  """  
      self.ReadingComment:str = obj["ReadingComment"]
      """  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  """  
      self.LocID:str = obj["LocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.ParentEquipID:str = obj["ParentEquipID"]
      """  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  """  
      self.LaborMeterOpt:str = obj["LaborMeterOpt"]
      """   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  """  
      self.ReadingDate:str = obj["ReadingDate"]
      """  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  """  
      self.ReadingTime:int = obj["ReadingTime"]
      """  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.AvgDailyUsage:int = obj["AvgDailyUsage"]
      self.GlobalEquip:bool = obj["GlobalEquip"]
      """  Marks this Equip as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NewMeter:int = obj["NewMeter"]
      """  External field used to enter a NEW meter reading valule.  When saved, it will update Equip.CurrentMeter, and them be set to zero for the next transaction.  """  
      self.NewReadingComment:str = obj["NewReadingComment"]
      """  Used to enter a comment related to the NEW meter reading.  When saved, this value updates current reading comment (Equip.ReadingComment) and is then blanked out.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MeterReadTableset:
   def __init__(self, obj):
      self.MeterRead:list[Erp_Tablesets_MeterReadRow] = obj["MeterRead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMeterReadTableset:
   def __init__(self, obj):
      self.MeterRead:list[Erp_Tablesets_MeterReadRow] = obj["MeterRead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   equipID
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MeterReadTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MeterReadTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MeterReadTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MeterReadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMeterRead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MeterReadTableset] = obj["ds"]
      pass

class GetNewMeterRead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MeterReadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMeterRead
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMeterRead:str = obj["whereClauseMeterRead"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MeterReadTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMeterReadTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMeterReadTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MeterReadTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MeterReadTableset] = obj["ds"]
      pass

      """  output parameters  """  

