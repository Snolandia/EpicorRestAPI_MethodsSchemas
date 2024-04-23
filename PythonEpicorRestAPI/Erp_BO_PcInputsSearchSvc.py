import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PcInputsSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputsSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches",headers=creds) as resp:
           return await resp.json()

async def post_PcInputsSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputsSearches_Company_ConfigID_InputName(Company, ConfigID, InputName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsSearch item
   Description: Calls GetByID to retrieve the PcInputsSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches(" + Company + "," + ConfigID + "," + InputName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputsSearches_Company_ConfigID_InputName(Company, ConfigID, InputName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputsSearch for the service
   Description: Calls UpdateExt to update PcInputsSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches(" + Company + "," + ConfigID + "," + InputName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputsSearches_Company_ConfigID_InputName(Company, ConfigID, InputName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputsSearch item
   Description: Call UpdateExt to delete PcInputsSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/PcInputsSearches(" + Company + "," + ConfigID + "," + InputName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePcInputs, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePcInputs=" + whereClausePcInputs
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(configID, inputName, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "configID=" + configID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "inputName=" + inputName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PcInputsSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsRow] = obj["value"]
      pass

class Erp_Tablesets_PcInputsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.TabOrder:int = obj["TabOrder"]
      """  The order that the tab function will step through the inputs.  """  
      self.DataType:str = obj["DataType"]
      """  The type of data that can be stored in the control.  """  
      self.FormatString:str = obj["FormatString"]
      """  The format for which the data will be stored.  """  
      self.InitVal:str = obj["InitVal"]
      """  The initial value for the control.  """  
      self.StatusText:str = obj["StatusText"]
      """  The popup help message that appears when the cursor is over the control.  """  
      self.Required:bool = obj["Required"]
      """  Determines if the contol must have a value before leaving the widget or the page of controls.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  On what page does the control exist.  """  
      self.SideLabel:str = obj["SideLabel"]
      """  The control's label.  """  
      self.xPos:int = obj["xPos"]
      """  The pixel position for the x axis.  """  
      self.yPos:int = obj["yPos"]
      """  The pixel position for the Y axis.  """  
      self.pWidth:int = obj["pWidth"]
      """  The pixel width of the control.  """  
      self.pHeight:int = obj["pHeight"]
      """  The pixel height of the control.  """  
      self.ControlType:str = obj["ControlType"]
      """  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the widget.  """  
      self.ListItems:str = obj["ListItems"]
      """  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  """  
      self.StartDec:int = obj["StartDec"]
      """  The starting decimal for a validated numeric fill-in.  """  
      self.EndDec:int = obj["EndDec"]
      """  The ending decimal for a validated numeric fill-in.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The precision used to determine the list of numbers to validate against.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date for a validated date fill-in.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date for a validated date fill-in.  """  
      self.ValList:str = obj["ValList"]
      """  The list of valid responses for a validated string input.  """  
      self.Horizontal:bool = obj["Horizontal"]
      """  If the control is a radio-set, is it a horizontal or vertical radio-set.  """  
      self.IsGlobal:bool = obj["IsGlobal"]
      """  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the control.  """  
      self.WebInputName:str = obj["WebInputName"]
      """  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  """  
      self.SummaryLabel:str = obj["SummaryLabel"]
      """  The label that will be used for the input when displaying a configuration summary.  """  
      self.DLRunProgram:bool = obj["DLRunProgram"]
      """  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  """  
      self.DLProgramName:str = obj["DLProgramName"]
      """  The Progress program used for building a dynamic list.  """  
      self.DLProgramInputs:str = obj["DLProgramInputs"]
      """  The inputs used for the Progress program used for building a dynamic list.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.HideInSummary:bool = obj["HideInSummary"]
      """  If TRUE then this input will not be shown in the configuration summary  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add On Leave expressions to this control  """  
      self.Invisible:bool = obj["Invisible"]
      """  If true, the input will not be displayed on the input page  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the input  """  
      self.GlobalInputVar:bool = obj["GlobalInputVar"]
      """  Global Input Variable  """  
      self.GlbInputVarName:str = obj["GlbInputVarName"]
      """  Global Input Variable Name  """  
      self.NoDispSummary:bool = obj["NoDispSummary"]
      """  Do not display input in Summary  """  
      self.ExternalRef:bool = obj["ExternalRef"]
      """  If true, allows entry to link input to inspection attribute data  """  
      self.AttributeID:str = obj["AttributeID"]
      """  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  """  
      self.UseMinValue:bool = obj["UseMinValue"]
      """  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseMaxValue:bool = obj["UseMaxValue"]
      """  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseIncrValue:bool = obj["UseIncrValue"]
      """  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseInitVal:bool = obj["UseInitVal"]
      """  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseToolTip:bool = obj["UseToolTip"]
      """  Setting to true will use the Tool Tip value from the specification detail table.  """  
      self.UseScreenLabel:bool = obj["UseScreenLabel"]
      """  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseListValues:bool = obj["UseListValues"]
      """  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.SmartPartSeq:int = obj["SmartPartSeq"]
      """  Defines the sequence of this input value in a smart part string sent for automatic processing.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.InitDate:str = obj["InitDate"]
      """  The initial value of a date field  """  
      self.InitDecimal:int = obj["InitDecimal"]
      """  The initial value of a decimal input  """  
      self.InitLogical:bool = obj["InitLogical"]
      """  The initial value for a logical input  """  
      self.DispCharVal:str = obj["DispCharVal"]
      """  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  """  
      self.IsGlobalInputVar:bool = obj["IsGlobalInputVar"]
      self.DspPageSeq:int = obj["DspPageSeq"]
      self.TestPlan:bool = obj["TestPlan"]
      self.AllowSmartString:bool = obj["AllowSmartString"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.TabOrder:int = obj["TabOrder"]
      """  The order that the tab function will step through the inputs.  """  
      self.DataType:str = obj["DataType"]
      """  The type of data that can be stored in the control.  """  
      self.FormatString:str = obj["FormatString"]
      """  The format for which the data will be stored.  """  
      self.InitVal:str = obj["InitVal"]
      """  The initial value for the control.  """  
      self.StatusText:str = obj["StatusText"]
      """  The popup help message that appears when the cursor is over the control.  """  
      self.Required:bool = obj["Required"]
      """  Determines if the contol must have a value before leaving the widget or the page of controls.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  On what page does the control exist.  """  
      self.SideLabel:str = obj["SideLabel"]
      """  The control's label.  """  
      self.xPos:int = obj["xPos"]
      """  The pixel position for the x axis.  """  
      self.yPos:int = obj["yPos"]
      """  The pixel position for the Y axis.  """  
      self.pWidth:int = obj["pWidth"]
      """  The pixel width of the control.  """  
      self.pHeight:int = obj["pHeight"]
      """  The pixel height of the control.  """  
      self.ControlType:str = obj["ControlType"]
      """  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the widget.  """  
      self.ListItems:str = obj["ListItems"]
      """  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  """  
      self.StartDec:int = obj["StartDec"]
      """  The starting decimal for a validated numeric fill-in.  """  
      self.EndDec:int = obj["EndDec"]
      """  The ending decimal for a validated numeric fill-in.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The precision used to determine the list of numbers to validate against.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date for a validated date fill-in.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date for a validated date fill-in.  """  
      self.ValList:str = obj["ValList"]
      """  The list of valid responses for a validated string input.  """  
      self.Horizontal:bool = obj["Horizontal"]
      """  If the control is a radio-set, is it a horizontal or vertical radio-set.  """  
      self.IsGlobal:bool = obj["IsGlobal"]
      """  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the control.  """  
      self.WebInputName:str = obj["WebInputName"]
      """  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  """  
      self.SummaryLabel:str = obj["SummaryLabel"]
      """  The label that will be used for the input when displaying a configuration summary.  """  
      self.DLRunProgram:bool = obj["DLRunProgram"]
      """  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  """  
      self.DLProgramName:str = obj["DLProgramName"]
      """  The Progress program used for building a dynamic list.  """  
      self.DLProgramInputs:str = obj["DLProgramInputs"]
      """  The inputs used for the Progress program used for building a dynamic list.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.HideInSummary:bool = obj["HideInSummary"]
      """  If TRUE then this input will not be shown in the configuration summary  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add On Leave expressions to this control  """  
      self.Invisible:bool = obj["Invisible"]
      """  If true, the input will not be displayed on the input page  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the input  """  
      self.GlobalInputVar:bool = obj["GlobalInputVar"]
      """  Global Input Variable  """  
      self.GlbInputVarName:str = obj["GlbInputVarName"]
      """  Global Input Variable Name  """  
      self.NoDispSummary:bool = obj["NoDispSummary"]
      """  Do not display input in Summary  """  
      self.ExternalRef:bool = obj["ExternalRef"]
      """  If true, allows entry to link input to inspection attribute data  """  
      self.AttributeID:str = obj["AttributeID"]
      """  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  """  
      self.UseMinValue:bool = obj["UseMinValue"]
      """  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseMaxValue:bool = obj["UseMaxValue"]
      """  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseIncrValue:bool = obj["UseIncrValue"]
      """  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseInitVal:bool = obj["UseInitVal"]
      """  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseToolTip:bool = obj["UseToolTip"]
      """  Setting to true will use the Tool Tip value from the specification detail table.  """  
      self.UseScreenLabel:bool = obj["UseScreenLabel"]
      """  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseListValues:bool = obj["UseListValues"]
      """  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.SmartPartSeq:int = obj["SmartPartSeq"]
      """  Defines the sequence of this input value in a smart part string sent for automatic processing.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.ShowDistinct:bool = obj["ShowDistinct"]
      """  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  """  
      self.DesignControlType:str = obj["DesignControlType"]
      """  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoSizeList:bool = obj["AutoSizeList"]
      """  AutoSizeList  """  
      self.ListWidth:int = obj["ListWidth"]
      """  ListWidth  """  
      self.ImageSource:str = obj["ImageSource"]
      """  ImageSource  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.Content:str = obj["Content"]
      self.DispCharVal:str = obj["DispCharVal"]
      """  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  """  
      self.DspPageSeq:int = obj["DspPageSeq"]
      self.FullInputName:str = obj["FullInputName"]
      """  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  """  
      self.ImageMapping:bool = obj["ImageMapping"]
      self.InitDate:str = obj["InitDate"]
      """  The initial value of a date field  """  
      self.InitDecimal:int = obj["InitDecimal"]
      """  The initial value of a decimal input  """  
      self.InitLogical:bool = obj["InitLogical"]
      """  The initial value for a logical input  """  
      self.InputRules:bool = obj["InputRules"]
      """  Indicates whether or not Input Rules have been defined.  """  
      self.InputType:str = obj["InputType"]
      """  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  """  
      self.IsGlobalInputVar:bool = obj["IsGlobalInputVar"]
      self.OnLaunch:str = obj["OnLaunch"]
      self.PageDisplaySeq:int = obj["PageDisplaySeq"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      """  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  """  
      self.ReadOnlyExpression:str = obj["ReadOnlyExpression"]
      self.TestPlan:bool = obj["TestPlan"]
      self.ImageURL:str = obj["ImageURL"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   configID
   inputName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PcInputsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.TabOrder:int = obj["TabOrder"]
      """  The order that the tab function will step through the inputs.  """  
      self.DataType:str = obj["DataType"]
      """  The type of data that can be stored in the control.  """  
      self.FormatString:str = obj["FormatString"]
      """  The format for which the data will be stored.  """  
      self.InitVal:str = obj["InitVal"]
      """  The initial value for the control.  """  
      self.StatusText:str = obj["StatusText"]
      """  The popup help message that appears when the cursor is over the control.  """  
      self.Required:bool = obj["Required"]
      """  Determines if the contol must have a value before leaving the widget or the page of controls.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  On what page does the control exist.  """  
      self.SideLabel:str = obj["SideLabel"]
      """  The control's label.  """  
      self.xPos:int = obj["xPos"]
      """  The pixel position for the x axis.  """  
      self.yPos:int = obj["yPos"]
      """  The pixel position for the Y axis.  """  
      self.pWidth:int = obj["pWidth"]
      """  The pixel width of the control.  """  
      self.pHeight:int = obj["pHeight"]
      """  The pixel height of the control.  """  
      self.ControlType:str = obj["ControlType"]
      """  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the widget.  """  
      self.ListItems:str = obj["ListItems"]
      """  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  """  
      self.StartDec:int = obj["StartDec"]
      """  The starting decimal for a validated numeric fill-in.  """  
      self.EndDec:int = obj["EndDec"]
      """  The ending decimal for a validated numeric fill-in.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The precision used to determine the list of numbers to validate against.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date for a validated date fill-in.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date for a validated date fill-in.  """  
      self.ValList:str = obj["ValList"]
      """  The list of valid responses for a validated string input.  """  
      self.Horizontal:bool = obj["Horizontal"]
      """  If the control is a radio-set, is it a horizontal or vertical radio-set.  """  
      self.IsGlobal:bool = obj["IsGlobal"]
      """  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the control.  """  
      self.WebInputName:str = obj["WebInputName"]
      """  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  """  
      self.SummaryLabel:str = obj["SummaryLabel"]
      """  The label that will be used for the input when displaying a configuration summary.  """  
      self.DLRunProgram:bool = obj["DLRunProgram"]
      """  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  """  
      self.DLProgramName:str = obj["DLProgramName"]
      """  The Progress program used for building a dynamic list.  """  
      self.DLProgramInputs:str = obj["DLProgramInputs"]
      """  The inputs used for the Progress program used for building a dynamic list.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.HideInSummary:bool = obj["HideInSummary"]
      """  If TRUE then this input will not be shown in the configuration summary  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add On Leave expressions to this control  """  
      self.Invisible:bool = obj["Invisible"]
      """  If true, the input will not be displayed on the input page  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the input  """  
      self.GlobalInputVar:bool = obj["GlobalInputVar"]
      """  Global Input Variable  """  
      self.GlbInputVarName:str = obj["GlbInputVarName"]
      """  Global Input Variable Name  """  
      self.NoDispSummary:bool = obj["NoDispSummary"]
      """  Do not display input in Summary  """  
      self.ExternalRef:bool = obj["ExternalRef"]
      """  If true, allows entry to link input to inspection attribute data  """  
      self.AttributeID:str = obj["AttributeID"]
      """  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  """  
      self.UseMinValue:bool = obj["UseMinValue"]
      """  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseMaxValue:bool = obj["UseMaxValue"]
      """  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseIncrValue:bool = obj["UseIncrValue"]
      """  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseInitVal:bool = obj["UseInitVal"]
      """  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseToolTip:bool = obj["UseToolTip"]
      """  Setting to true will use the Tool Tip value from the specification detail table.  """  
      self.UseScreenLabel:bool = obj["UseScreenLabel"]
      """  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseListValues:bool = obj["UseListValues"]
      """  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.SmartPartSeq:int = obj["SmartPartSeq"]
      """  Defines the sequence of this input value in a smart part string sent for automatic processing.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.InitDate:str = obj["InitDate"]
      """  The initial value of a date field  """  
      self.InitDecimal:int = obj["InitDecimal"]
      """  The initial value of a decimal input  """  
      self.InitLogical:bool = obj["InitLogical"]
      """  The initial value for a logical input  """  
      self.DispCharVal:str = obj["DispCharVal"]
      """  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  """  
      self.IsGlobalInputVar:bool = obj["IsGlobalInputVar"]
      self.DspPageSeq:int = obj["DspPageSeq"]
      self.TestPlan:bool = obj["TestPlan"]
      self.AllowSmartString:bool = obj["AllowSmartString"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsListTableset:
   def __init__(self, obj):
      self.PcInputsList:list[Erp_Tablesets_PcInputsListRow] = obj["PcInputsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcInputsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.TabOrder:int = obj["TabOrder"]
      """  The order that the tab function will step through the inputs.  """  
      self.DataType:str = obj["DataType"]
      """  The type of data that can be stored in the control.  """  
      self.FormatString:str = obj["FormatString"]
      """  The format for which the data will be stored.  """  
      self.InitVal:str = obj["InitVal"]
      """  The initial value for the control.  """  
      self.StatusText:str = obj["StatusText"]
      """  The popup help message that appears when the cursor is over the control.  """  
      self.Required:bool = obj["Required"]
      """  Determines if the contol must have a value before leaving the widget or the page of controls.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  On what page does the control exist.  """  
      self.SideLabel:str = obj["SideLabel"]
      """  The control's label.  """  
      self.xPos:int = obj["xPos"]
      """  The pixel position for the x axis.  """  
      self.yPos:int = obj["yPos"]
      """  The pixel position for the Y axis.  """  
      self.pWidth:int = obj["pWidth"]
      """  The pixel width of the control.  """  
      self.pHeight:int = obj["pHeight"]
      """  The pixel height of the control.  """  
      self.ControlType:str = obj["ControlType"]
      """  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the widget.  """  
      self.ListItems:str = obj["ListItems"]
      """  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  """  
      self.StartDec:int = obj["StartDec"]
      """  The starting decimal for a validated numeric fill-in.  """  
      self.EndDec:int = obj["EndDec"]
      """  The ending decimal for a validated numeric fill-in.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The precision used to determine the list of numbers to validate against.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date for a validated date fill-in.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date for a validated date fill-in.  """  
      self.ValList:str = obj["ValList"]
      """  The list of valid responses for a validated string input.  """  
      self.Horizontal:bool = obj["Horizontal"]
      """  If the control is a radio-set, is it a horizontal or vertical radio-set.  """  
      self.IsGlobal:bool = obj["IsGlobal"]
      """  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the control.  """  
      self.WebInputName:str = obj["WebInputName"]
      """  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  """  
      self.SummaryLabel:str = obj["SummaryLabel"]
      """  The label that will be used for the input when displaying a configuration summary.  """  
      self.DLRunProgram:bool = obj["DLRunProgram"]
      """  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  """  
      self.DLProgramName:str = obj["DLProgramName"]
      """  The Progress program used for building a dynamic list.  """  
      self.DLProgramInputs:str = obj["DLProgramInputs"]
      """  The inputs used for the Progress program used for building a dynamic list.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.HideInSummary:bool = obj["HideInSummary"]
      """  If TRUE then this input will not be shown in the configuration summary  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add On Leave expressions to this control  """  
      self.Invisible:bool = obj["Invisible"]
      """  If true, the input will not be displayed on the input page  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the input  """  
      self.GlobalInputVar:bool = obj["GlobalInputVar"]
      """  Global Input Variable  """  
      self.GlbInputVarName:str = obj["GlbInputVarName"]
      """  Global Input Variable Name  """  
      self.NoDispSummary:bool = obj["NoDispSummary"]
      """  Do not display input in Summary  """  
      self.ExternalRef:bool = obj["ExternalRef"]
      """  If true, allows entry to link input to inspection attribute data  """  
      self.AttributeID:str = obj["AttributeID"]
      """  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  """  
      self.UseMinValue:bool = obj["UseMinValue"]
      """  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseMaxValue:bool = obj["UseMaxValue"]
      """  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseIncrValue:bool = obj["UseIncrValue"]
      """  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseInitVal:bool = obj["UseInitVal"]
      """  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseToolTip:bool = obj["UseToolTip"]
      """  Setting to true will use the Tool Tip value from the specification detail table.  """  
      self.UseScreenLabel:bool = obj["UseScreenLabel"]
      """  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseListValues:bool = obj["UseListValues"]
      """  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.SmartPartSeq:int = obj["SmartPartSeq"]
      """  Defines the sequence of this input value in a smart part string sent for automatic processing.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.ShowDistinct:bool = obj["ShowDistinct"]
      """  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  """  
      self.DesignControlType:str = obj["DesignControlType"]
      """  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoSizeList:bool = obj["AutoSizeList"]
      """  AutoSizeList  """  
      self.ListWidth:int = obj["ListWidth"]
      """  ListWidth  """  
      self.ImageSource:str = obj["ImageSource"]
      """  ImageSource  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.Content:str = obj["Content"]
      self.DispCharVal:str = obj["DispCharVal"]
      """  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  """  
      self.DspPageSeq:int = obj["DspPageSeq"]
      self.FullInputName:str = obj["FullInputName"]
      """  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  """  
      self.ImageMapping:bool = obj["ImageMapping"]
      self.InitDate:str = obj["InitDate"]
      """  The initial value of a date field  """  
      self.InitDecimal:int = obj["InitDecimal"]
      """  The initial value of a decimal input  """  
      self.InitLogical:bool = obj["InitLogical"]
      """  The initial value for a logical input  """  
      self.InputRules:bool = obj["InputRules"]
      """  Indicates whether or not Input Rules have been defined.  """  
      self.InputType:str = obj["InputType"]
      """  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  """  
      self.IsGlobalInputVar:bool = obj["IsGlobalInputVar"]
      self.OnLaunch:str = obj["OnLaunch"]
      self.PageDisplaySeq:int = obj["PageDisplaySeq"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      """  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  """  
      self.ReadOnlyExpression:str = obj["ReadOnlyExpression"]
      self.TestPlan:bool = obj["TestPlan"]
      self.ImageURL:str = obj["ImageURL"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsSearchTableset:
   def __init__(self, obj):
      self.PcInputs:list[Erp_Tablesets_PcInputsRow] = obj["PcInputs"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPcInputsSearchTableset:
   def __init__(self, obj):
      self.PcInputs:list[Erp_Tablesets_PcInputsRow] = obj["PcInputs"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   configID
   inputName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcInputsSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PcInputsSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PcInputsSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PcInputsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPcInputs_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcInputsSearchTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcInputs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcInputsSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePcInputs
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePcInputs:str = obj["whereClausePcInputs"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcInputsSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPcInputsSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPcInputsSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcInputsSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcInputsSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

