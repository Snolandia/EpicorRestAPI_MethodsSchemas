import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgCtrlOverlayPCIDValidateSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PkgCtrlOverlayPCIDValidates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgCtrlOverlayPCIDValidates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgCtrlOverlayPCIDValidates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgCtrlOverlayPCIDValidates",headers=creds) as resp:
           return await resp.json()

async def post_PkgCtrlOverlayPCIDValidates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgCtrlOverlayPCIDValidates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgCtrlOverlayPCIDValidates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgCtrlOverlayPCIDValidates_Company_PCID(Company, PCID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgCtrlOverlayPCIDValidate item
   Description: Calls GetByID to retrieve the PkgCtrlOverlayPCIDValidate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgCtrlOverlayPCIDValidate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgCtrlOverlayPCIDValidates(" + Company + "," + PCID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgCtrlOverlayPCIDValidates_Company_PCID(Company, PCID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgCtrlOverlayPCIDValidate for the service
   Description: Calls UpdateExt to update PkgCtrlOverlayPCIDValidate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgCtrlOverlayPCIDValidate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgCtrlOverlayPCIDValidates(" + Company + "," + PCID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgCtrlOverlayPCIDValidates_Company_PCID(Company, PCID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgCtrlOverlayPCIDValidate item
   Description: Call UpdateExt to delete PkgCtrlOverlayPCIDValidate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgCtrlOverlayPCIDValidate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgCtrlOverlayPCIDValidates(" + Company + "," + PCID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlItems(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlItems
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgControlItems",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlItems(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlItemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlItemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgControlItems", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlItems_Company_PCID_PCIDItemSeq(Company, PCID, PCIDItemSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlItem item
   Description: Calls GetByID to retrieve the PkgControlItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param PCIDItemSeq: Desc: PCIDItemSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgControlItems(" + Company + "," + PCID + "," + PCIDItemSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlItems_Company_PCID_PCIDItemSeq(Company, PCID, PCIDItemSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlItem for the service
   Description: Calls UpdateExt to update PkgControlItem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param PCIDItemSeq: Desc: PCIDItemSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlItemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgControlItems(" + Company + "," + PCID + "," + PCIDItemSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlItems_Company_PCID_PCIDItemSeq(Company, PCID, PCIDItemSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlItem item
   Description: Call UpdateExt to delete PkgControlItem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlItem
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PCID: Desc: PCID   Required: True   Allow empty value : True
      :param PCIDItemSeq: Desc: PCIDItemSeq   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/PkgControlItems(" + Company + "," + PCID + "," + PCIDItemSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlHeaderListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePkgControlHeader, whereClausePkgControlItem, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClausePkgControlHeader=" + whereClausePkgControlHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePkgControlItem=" + whereClausePkgControlItem
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(pcID, epicorHeaders = None):
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
   params += "pcID=" + pcID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePCID
   Description: Makes sure the first PCID provided by the user is valid, according to the following:
- PCID is in Epicor
- Label Type = “INDIVIDUAL” OR “INTERNAL“
- Label Status = “STOCK”
- Overlaid = false
   OperationID: ValidatePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOverlayPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOverlayPCID
   Description: Makes sure the second PCID provided by the user is valid.
   OperationID: ValidateOverlayPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOverlayPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOverlayPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OverlayPCIDValidationProcess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OverlayPCIDValidationProcess
   Description: Verify if the Items of the PCIDs provided match.
   OperationID: OverlayPCIDValidationProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OverlayPCIDValidationProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OverlayPCIDValidationProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPkgControlHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPkgControlHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPkgControlItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPkgControlItem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgCtrlOverlayPCIDValidateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlHeaderListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlHeaderListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlHeaderRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlItemRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlItemRow] = obj["value"]
      pass

class Erp_Tablesets_PkgControlHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.Plant:str = obj["Plant"]
      """  Site where the PCID is currently located.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.ReturnToWarehouseCode:str = obj["ReturnToWarehouseCode"]
      """  Warehouse where the PCID return stock needs to be returned to.  """  
      self.ReturnToBinNum:str = obj["ReturnToBinNum"]
      """  Warehouse Bin where the PCID return stock needs to be returned to.  """  
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      """  PCID current status.  """  
      self.PkgControlPriorStatus:str = obj["PkgControlPriorStatus"]
      """  PCID prior status.  """  
      self.LabelPrintControlStatus:str = obj["LabelPrintControlStatus"]
      """  Label Print Control status.  """  
      self.LabelPrintControlPriorStatus:str = obj["LabelPrintControlPriorStatus"]
      """  Label Print Control prior status.  """  
      self.AllowParentPCID:bool = obj["AllowParentPCID"]
      """  If false then PCID is a single-level PCID that cannot be associated with a Parent.  """  
      self.AllowMixedParts:bool = obj["AllowMixedParts"]
      """  If false then PCID must contain only one PartNum.  """  
      self.AllowMixedLots:bool = obj["AllowMixedLots"]
      """  If false then PCID must contain only one LotNum for each Part on the PCID.  """  
      self.AllowMixedUOMs:bool = obj["AllowMixedUOMs"]
      """  If false then PCID must contain only one UOM per Part on the PCID.  """  
      self.AllowMixedChildPCIDs:bool = obj["AllowMixedChildPCIDs"]
      """  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  """  
      self.AllowMultipleSerialNumPerPCID:bool = obj["AllowMultipleSerialNumPerPCID"]
      """  If false then PCID must contain only one Serial Number per PCID.  """  
      self.LabelPrintControlled:bool = obj["LabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.LabelPrintCounter:bool = obj["LabelPrintCounter"]
      """  If false then the number of PCID label prints will not be tracked.  """  
      self.AllowVoids:bool = obj["AllowVoids"]
      """  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  """  
      self.AllowDeletes:bool = obj["AllowDeletes"]
      """  If false then PkgControlHeader and PkgControlItem cannot be deleted.  """  
      self.ArchivePCIDHistory:bool = obj["ArchivePCIDHistory"]
      """  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.LWHDimensionUOM:str = obj["LWHDimensionUOM"]
      """  User defined code which uniquely identifies the UOM for length, width, and height.  """  
      self.Length:int = obj["Length"]
      """  Length dimension.  """  
      self.Width:int = obj["Width"]
      """  Width dimension.  """  
      self.Height:int = obj["Height"]
      """  Height dimension.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """  User defined code which uniquely identifies the UOM for volume.  """  
      self.Volume:int = obj["Volume"]
      """  Volume.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  User defined code which uniquely identifies the UOM for weight.  """  
      self.MaximumWeight:int = obj["MaximumWeight"]
      """  Maximum Weight.  """  
      self.CalculatedWeight:int = obj["CalculatedWeight"]
      """  Calculated Weight.  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  The total weight of the parts and the container combined.  """  
      self.MaximumStack:int = obj["MaximumStack"]
      """  Maximum number of PCIDs allowed if vertically stacked.  """  
      self.PositionSeq:int = obj["PositionSeq"]
      """  Position Sequence within a parent PCID.  """  
      self.TrailerID:str = obj["TrailerID"]
      """  Trailer ID.  """  
      self.SecuritySealID:str = obj["SecuritySealID"]
      """  Bond or Security Seal ID.  """  
      self.RawPCIDLicensePlate:str = obj["RawPCIDLicensePlate"]
      """  Raw PCID as scanned or generated.  """  
      self.GS1128:str = obj["GS1128"]
      """  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  """  
      self.PkgControlCollapseCounter:int = obj["PkgControlCollapseCounter"]
      """  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  System date and time when the row was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this row.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  System date and time when the row was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID that last updated this row.  """  
      self.LastPCIDScanned:str = obj["LastPCIDScanned"]
      """  Last PCID Scanned.  """  
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.AutoPrint:bool = obj["AutoPrint"]
      """  Flag used to fire the auto print rule that will print the labels.  """  
      self.LPCCreatedDate:str = obj["LPCCreatedDate"]
      """  System date and time when the row was created.  """  
      self.LPCCreatedBy:str = obj["LPCCreatedBy"]
      """  The user ID that created this record.  """  
      self.LPCPrinterID:str = obj["LPCPrinterID"]
      """  Printer ID that printed the label.  """  
      self.LPCPrintedBy:str = obj["LPCPrintedBy"]
      """  User that printed the label.  """  
      self.LPCPrintedFromTx:str = obj["LPCPrintedFromTx"]
      """  Label feature. Displays what transaction the label was printed from.  """  
      self.LPCPrintedFromTxType:str = obj["LPCPrintedFromTxType"]
      """  Ad Hoc feature. Displays what transaction type the label was printed from.  """  
      self.LPCJobNum:str = obj["LPCJobNum"]
      """  The job for which the label was printed.  """  
      self.LPCOprSeq:int = obj["LPCOprSeq"]
      """  The operation sequence for which the label was printed.  """  
      self.LPCAssemblySeq:int = obj["LPCAssemblySeq"]
      """  The assembly sequence for which the label was printed.  """  
      self.LPCShift:int = obj["LPCShift"]
      """  Shift that the label was created on or shift entered in Ad Hoc print program.  """  
      self.LPCOperatorEmpID:str = obj["LPCOperatorEmpID"]
      """  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  """  
      self.OriginalSourcePCID:str = obj["OriginalSourcePCID"]
      """  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  """  
      self.OverlaidByPCID:str = obj["OverlaidByPCID"]
      """  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  """  
      self.Overlaid:bool = obj["Overlaid"]
      """  Set to True when PCID has been overlaid using the overlay feature.  """  
      self.ContainerPartial:bool = obj["ContainerPartial"]
      """  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  """  
      self.ContainerRepacked:bool = obj["ContainerRepacked"]
      """  If true the container was repacked.  """  
      self.ContainerReturnable:bool = obj["ContainerReturnable"]
      """  If true the container used is a returnable container.  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Vendor ID for the Customer being Shipped To.  """  
      self.PlantName:str = obj["PlantName"]
      """  Site Name.  """  
      self.PlantAddress1:str = obj["PlantAddress1"]
      """  Site Address line 1.  """  
      self.PlantAddress2:str = obj["PlantAddress2"]
      """  Site Address line 2.  """  
      self.PlantAddress3:str = obj["PlantAddress3"]
      """  Site Address line 3.  """  
      self.PlantCity:str = obj["PlantCity"]
      """  Site City.  """  
      self.PlantState:str = obj["PlantState"]
      """  Site State.  """  
      self.PlantZip:str = obj["PlantZip"]
      """  Site Zip.  """  
      self.PlantCountryNum:int = obj["PlantCountryNum"]
      """  Site Country Number.  """  
      self.PlantCountryDesc:str = obj["PlantCountryDesc"]
      """  Site Country Description.  """  
      self.PlantPhone:str = obj["PlantPhone"]
      """  Site Phone.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack Number if applicable.  """  
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      """  Ship To Customer Container Part Number.  """  
      self.EDIShipToNum:str = obj["EDIShipToNum"]
      """  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Ship To Number.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Name of the Ship To that the PCID is going to.  """  
      self.ShipToAddress1:str = obj["ShipToAddress1"]
      """  Address line 1 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress2:str = obj["ShipToAddress2"]
      """  Address line 2 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress3:str = obj["ShipToAddress3"]
      """  Address line 3 of the Ship To that the PCID is going to.  """  
      self.ShipToCity:str = obj["ShipToCity"]
      """  City of the Ship To that the PCID is going to.  """  
      self.ShipToState:str = obj["ShipToState"]
      """  State of the Ship To that the PCID is going to.  """  
      self.ShipToZip:str = obj["ShipToZip"]
      """  Zip of the Ship To that the PCID is going to.  """  
      self.ShipToCountryNum:int = obj["ShipToCountryNum"]
      """  Country number of the Ship To that the PCID is going to.  """  
      self.ShipToCountryDesc:str = obj["ShipToCountryDesc"]
      """  Country of the Ship To that the PCID is going to.  """  
      self.ShipToDock:str = obj["ShipToDock"]
      """  The dock that the parts should be shipped to.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID.  """  
      self.VendorPurPoint:str = obj["VendorPurPoint"]
      """  Vendor Purchase Point.  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  Vendor Address line 1.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Vendor Address line 2.  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Vendor Address line 3.  """  
      self.VendorCity:str = obj["VendorCity"]
      """  Vendor City.  """  
      self.VendorState:str = obj["VendorState"]
      """  Vendor State.  """  
      self.VendorZip:str = obj["VendorZip"]
      """  Vendor Zip.  """  
      self.VendorCountryNum:int = obj["VendorCountryNum"]
      """  Vendor Country Number.  """  
      self.VendorCountryDesc:str = obj["VendorCountryDesc"]
      """  Vendor Country Description.  """  
      self.OurDock:str = obj["OurDock"]
      """  Our Dock ID.  """  
      self.LabelValue01:str = obj["LabelValue01"]
      """  Value to display on package control label.  """  
      self.LabelValue02:str = obj["LabelValue02"]
      """  Value to display on package control label.  """  
      self.LabelValue03:str = obj["LabelValue03"]
      """  Value to display on package control label.  """  
      self.LabelValue04:str = obj["LabelValue04"]
      """  Value to display on package control label.  """  
      self.LabelValue05:str = obj["LabelValue05"]
      """  Value to display on package control label.  """  
      self.LabelValue06:str = obj["LabelValue06"]
      """  Value to display on package control label.  """  
      self.LabelValue07:str = obj["LabelValue07"]
      """  Value to display on package control label.  """  
      self.LabelValue08:str = obj["LabelValue08"]
      """  Value to display on package control label.  """  
      self.LabelValue09:str = obj["LabelValue09"]
      """  Value to display on package control label.  """  
      self.LabelValue10:str = obj["LabelValue10"]
      """  Value to display on package control label.  """  
      self.LabelValue11:str = obj["LabelValue11"]
      """  Value to display on package control label.  """  
      self.LabelValue12:str = obj["LabelValue12"]
      """  Value to display on package control label.  """  
      self.LabelValue13:str = obj["LabelValue13"]
      """  Value to display on package control label.  """  
      self.LabelValue14:str = obj["LabelValue14"]
      """  Value to display on package control label.  """  
      self.LabelValue15:str = obj["LabelValue15"]
      """  Value to display on package control label.  """  
      self.LabelValue16:str = obj["LabelValue16"]
      """  Value to display on package control label.  """  
      self.LabelValue17:str = obj["LabelValue17"]
      """  Value to display on package control label.  """  
      self.LabelValue18:str = obj["LabelValue18"]
      """  Value to display on package control label.  """  
      self.LabelValue19:str = obj["LabelValue19"]
      """  Value to display on package control label.  """  
      self.LabelValue20:str = obj["LabelValue20"]
      """  Value to display on package control label.  """  
      self.LabelValue21:str = obj["LabelValue21"]
      """  Value to display on package control label.  """  
      self.LabelValue22:str = obj["LabelValue22"]
      """  Value to display on package control label.  """  
      self.LabelValue23:str = obj["LabelValue23"]
      """  Value to display on package control label.  """  
      self.LabelValue24:str = obj["LabelValue24"]
      """  Value to display on package control label.  """  
      self.LabelValue25:str = obj["LabelValue25"]
      """  Value to display on package control label.  """  
      self.LabelValue26:str = obj["LabelValue26"]
      """  Value to display on package control label.  """  
      self.LabelValue27:str = obj["LabelValue27"]
      """  Value to display on package control label.  """  
      self.LabelValue28:str = obj["LabelValue28"]
      """  Value to display on package control label.  """  
      self.LabelValue29:str = obj["LabelValue29"]
      """  Value to display on package control label.  """  
      self.LabelValue30:str = obj["LabelValue30"]
      """  Value to display on package control label.  """  
      self.PkgControlCharacter01:str = obj["PkgControlCharacter01"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter02:str = obj["PkgControlCharacter02"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter03:str = obj["PkgControlCharacter03"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter04:str = obj["PkgControlCharacter04"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter05:str = obj["PkgControlCharacter05"]
      """  Reserved for development use.  """  
      self.PkgControlDate01:str = obj["PkgControlDate01"]
      """  Reserved for development use.  """  
      self.PkgControlDate02:str = obj["PkgControlDate02"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean01:bool = obj["PkgControlBoolean01"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean02:bool = obj["PkgControlBoolean02"]
      """  Reserved for development use.  """  
      self.PkgControlInteger01:int = obj["PkgControlInteger01"]
      """  Reserved for development use.  """  
      self.PkgControlInteger02:int = obj["PkgControlInteger02"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal01:int = obj["PkgControlDecimal01"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal02:int = obj["PkgControlDecimal02"]
      """  Reserved for development use.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.ExternalLength:int = obj["ExternalLength"]
      """  External Length dimension.  """  
      self.ExternalWidth:int = obj["ExternalWidth"]
      """  External Width dimension.  """  
      self.ExternalHeight:int = obj["ExternalHeight"]
      """  External Height dimension.  """  
      self.ExternalVolume:int = obj["ExternalVolume"]
      """  External Volume.  """  
      self.TareWeight:int = obj["TareWeight"]
      """  Tare Weight.  """  
      self.LabelPrintCount:int = obj["LabelPrintCount"]
      """  Incremental tally of number of times PCID label has been printed.  """  
      self.TrackExpendable:bool = obj["TrackExpendable"]
      """  Indicates if the expendable PCID will be tracked.  """  
      self.TrackReturnable:bool = obj["TrackReturnable"]
      """  Indicates if the returnable PCID will be tracked.  """  
      self.LabelType:str = obj["LabelType"]
      """  Label Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustNum:int = obj["CustNum"]
      """  Ship To Customer Number.  """  
      self.ContainerExpendable:bool = obj["ContainerExpendable"]
      """  Indicates if the PCID is expendable.  """  
      self.CustID:str = obj["CustID"]
      """  Ship To Customer ID.  """  
      self.CustName:str = obj["CustName"]
      """  Ship To Customer Name.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor Name.  """  
      self.VendorPPName:str = obj["VendorPPName"]
      """  Vendor Purchase Point Name.  """  
      self.AdhocStagedInventory:bool = obj["AdhocStagedInventory"]
      """  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  """  
      self.UpdatedByEmpID:str = obj["UpdatedByEmpID"]
      """  UpdatedByEmpID  """  
      self.RawBarcodeScan:str = obj["RawBarcodeScan"]
      """  Raw Barcode Scan prior to execution of any extract logic.  """  
      self.OutboundContainer:bool = obj["OutboundContainer"]
      """  OutboundContainer  """  
      self.BeforePackPkgControlStatus:str = obj["BeforePackPkgControlStatus"]
      """  PkgControlStatus value prior to being added to a pack.  """  
      self.BeforePackLabelPrintControlStatus:str = obj["BeforePackLabelPrintControlStatus"]
      """  LabelPrintControlStatus value prior to being added to a pack.  """  
      self.PackedFromSource:str = obj["PackedFromSource"]
      """  To indicate the source process when a PCID was added to a pack.  """  
      self.LastCountedDate:str = obj["LastCountedDate"]
      """  Date last counted.  Updated during the cycle count Posting Process.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  TFPackNum  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.Plant:str = obj["Plant"]
      """  Site where the PCID is currently located.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.ReturnToWarehouseCode:str = obj["ReturnToWarehouseCode"]
      """  Warehouse where the PCID return stock needs to be returned to.  """  
      self.ReturnToBinNum:str = obj["ReturnToBinNum"]
      """  Warehouse Bin where the PCID return stock needs to be returned to.  """  
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      """  PCID current status.  """  
      self.PkgControlPriorStatus:str = obj["PkgControlPriorStatus"]
      """  PCID prior status.  """  
      self.LabelPrintControlStatus:str = obj["LabelPrintControlStatus"]
      """  Label Print Control status.  """  
      self.LabelPrintControlPriorStatus:str = obj["LabelPrintControlPriorStatus"]
      """  Label Print Control prior status.  """  
      self.AllowParentPCID:bool = obj["AllowParentPCID"]
      """  If false then PCID is a single-level PCID that cannot be associated with a Parent.  """  
      self.AllowMixedParts:bool = obj["AllowMixedParts"]
      """  If false then PCID must contain only one PartNum.  """  
      self.AllowMixedLots:bool = obj["AllowMixedLots"]
      """  If false then PCID must contain only one LotNum for each Part on the PCID.  """  
      self.AllowMixedUOMs:bool = obj["AllowMixedUOMs"]
      """  If false then PCID must contain only one UOM per Part on the PCID.  """  
      self.AllowMixedChildPCIDs:bool = obj["AllowMixedChildPCIDs"]
      """  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  """  
      self.AllowMultipleSerialNumPerPCID:bool = obj["AllowMultipleSerialNumPerPCID"]
      """  If false then PCID must contain only one Serial Number per PCID.  """  
      self.LabelPrintControlled:bool = obj["LabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.LabelPrintCounter:bool = obj["LabelPrintCounter"]
      """  If false then the number of PCID label prints will not be tracked.  """  
      self.AllowVoids:bool = obj["AllowVoids"]
      """  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  """  
      self.AllowDeletes:bool = obj["AllowDeletes"]
      """  If false then PkgControlHeader and PkgControlItem cannot be deleted.  """  
      self.ArchivePCIDHistory:bool = obj["ArchivePCIDHistory"]
      """  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.LWHDimensionUOM:str = obj["LWHDimensionUOM"]
      """  User defined code which uniquely identifies the UOM for length, width, and height.  """  
      self.Length:int = obj["Length"]
      """  Length dimension.  """  
      self.Width:int = obj["Width"]
      """  Width dimension.  """  
      self.Height:int = obj["Height"]
      """  Height dimension.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """  User defined code which uniquely identifies the UOM for volume.  """  
      self.Volume:int = obj["Volume"]
      """  Volume.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  User defined code which uniquely identifies the UOM for weight.  """  
      self.MaximumWeight:int = obj["MaximumWeight"]
      """  Maximum Weight.  """  
      self.CalculatedWeight:int = obj["CalculatedWeight"]
      """  Calculated Weight.  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  The total weight of the parts and the container combined.  """  
      self.MaximumStack:int = obj["MaximumStack"]
      """  Maximum number of PCIDs allowed if vertically stacked.  """  
      self.PositionSeq:int = obj["PositionSeq"]
      """  Position Sequence within a parent PCID.  """  
      self.TrailerID:str = obj["TrailerID"]
      """  Trailer ID.  """  
      self.SecuritySealID:str = obj["SecuritySealID"]
      """  Bond or Security Seal ID.  """  
      self.RawPCIDLicensePlate:str = obj["RawPCIDLicensePlate"]
      """  Raw PCID as scanned or generated.  """  
      self.GS1128:str = obj["GS1128"]
      """  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  """  
      self.PkgControlCollapseCounter:int = obj["PkgControlCollapseCounter"]
      """  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  System date and time when the row was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this row.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  System date and time when the row was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID that last updated this row.  """  
      self.LastPCIDScanned:str = obj["LastPCIDScanned"]
      """  Last PCID Scanned.  """  
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.AutoPrint:bool = obj["AutoPrint"]
      """  Flag used to fire the auto print rule that will print the labels.  """  
      self.LPCCreatedDate:str = obj["LPCCreatedDate"]
      """  System date and time when the row was created.  """  
      self.LPCCreatedBy:str = obj["LPCCreatedBy"]
      """  The user ID that created this record.  """  
      self.LPCPrinterID:str = obj["LPCPrinterID"]
      """  Printer ID that printed the label.  """  
      self.LPCPrintedBy:str = obj["LPCPrintedBy"]
      """  User that printed the label.  """  
      self.LPCPrintedFromTx:str = obj["LPCPrintedFromTx"]
      """  Label feature. Displays what transaction the label was printed from.  """  
      self.LPCPrintedFromTxType:str = obj["LPCPrintedFromTxType"]
      """  Ad Hoc feature. Displays what transaction type the label was printed from.  """  
      self.LPCJobNum:str = obj["LPCJobNum"]
      """  The job for which the label was printed.  """  
      self.LPCOprSeq:int = obj["LPCOprSeq"]
      """  The operation sequence for which the label was printed.  """  
      self.LPCAssemblySeq:int = obj["LPCAssemblySeq"]
      """  The assembly sequence for which the label was printed.  """  
      self.LPCShift:int = obj["LPCShift"]
      """  Shift that the label was created on or shift entered in Ad Hoc print program.  """  
      self.LPCOperatorEmpID:str = obj["LPCOperatorEmpID"]
      """  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  """  
      self.OriginalSourcePCID:str = obj["OriginalSourcePCID"]
      """  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  """  
      self.OverlaidByPCID:str = obj["OverlaidByPCID"]
      """  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  """  
      self.Overlaid:bool = obj["Overlaid"]
      """  Set to True when PCID has been overlaid using the overlay feature.  """  
      self.ContainerPartial:bool = obj["ContainerPartial"]
      """  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  """  
      self.ContainerRepacked:bool = obj["ContainerRepacked"]
      """  If true the container was repacked.  """  
      self.ContainerReturnable:bool = obj["ContainerReturnable"]
      """  If true the container used is a returnable container.  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Vendor ID for the Customer being Shipped To.  """  
      self.PlantName:str = obj["PlantName"]
      """  Site Name.  """  
      self.PlantAddress1:str = obj["PlantAddress1"]
      """  Site Address line 1.  """  
      self.PlantAddress2:str = obj["PlantAddress2"]
      """  Site Address line 2.  """  
      self.PlantAddress3:str = obj["PlantAddress3"]
      """  Site Address line 3.  """  
      self.PlantCity:str = obj["PlantCity"]
      """  Site City.  """  
      self.PlantState:str = obj["PlantState"]
      """  Site State.  """  
      self.PlantZip:str = obj["PlantZip"]
      """  Site Zip.  """  
      self.PlantCountryNum:int = obj["PlantCountryNum"]
      """  Site Country Number.  """  
      self.PlantCountryDesc:str = obj["PlantCountryDesc"]
      """  Site Country Description.  """  
      self.PlantPhone:str = obj["PlantPhone"]
      """  Site Phone.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack Number if applicable.  """  
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      """  Ship To Customer Container Part Number.  """  
      self.EDIShipToNum:str = obj["EDIShipToNum"]
      """  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Ship To Number.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Name of the Ship To that the PCID is going to.  """  
      self.ShipToAddress1:str = obj["ShipToAddress1"]
      """  Address line 1 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress2:str = obj["ShipToAddress2"]
      """  Address line 2 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress3:str = obj["ShipToAddress3"]
      """  Address line 3 of the Ship To that the PCID is going to.  """  
      self.ShipToCity:str = obj["ShipToCity"]
      """  City of the Ship To that the PCID is going to.  """  
      self.ShipToState:str = obj["ShipToState"]
      """  State of the Ship To that the PCID is going to.  """  
      self.ShipToZip:str = obj["ShipToZip"]
      """  Zip of the Ship To that the PCID is going to.  """  
      self.ShipToCountryNum:int = obj["ShipToCountryNum"]
      """  Country number of the Ship To that the PCID is going to.  """  
      self.ShipToCountryDesc:str = obj["ShipToCountryDesc"]
      """  Country of the Ship To that the PCID is going to.  """  
      self.ShipToDock:str = obj["ShipToDock"]
      """  The dock that the parts should be shipped to.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID.  """  
      self.VendorPurPoint:str = obj["VendorPurPoint"]
      """  Vendor Purchase Point.  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  Vendor Address line 1.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Vendor Address line 2.  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Vendor Address line 3.  """  
      self.VendorCity:str = obj["VendorCity"]
      """  Vendor City.  """  
      self.VendorState:str = obj["VendorState"]
      """  Vendor State.  """  
      self.VendorZip:str = obj["VendorZip"]
      """  Vendor Zip.  """  
      self.VendorCountryNum:int = obj["VendorCountryNum"]
      """  Vendor Country Number.  """  
      self.VendorCountryDesc:str = obj["VendorCountryDesc"]
      """  Vendor Country Description.  """  
      self.OurDock:str = obj["OurDock"]
      """  Our Dock ID.  """  
      self.LabelValue01:str = obj["LabelValue01"]
      """  Value to display on package control label.  """  
      self.LabelValue02:str = obj["LabelValue02"]
      """  Value to display on package control label.  """  
      self.LabelValue03:str = obj["LabelValue03"]
      """  Value to display on package control label.  """  
      self.LabelValue04:str = obj["LabelValue04"]
      """  Value to display on package control label.  """  
      self.LabelValue05:str = obj["LabelValue05"]
      """  Value to display on package control label.  """  
      self.LabelValue06:str = obj["LabelValue06"]
      """  Value to display on package control label.  """  
      self.LabelValue07:str = obj["LabelValue07"]
      """  Value to display on package control label.  """  
      self.LabelValue08:str = obj["LabelValue08"]
      """  Value to display on package control label.  """  
      self.LabelValue09:str = obj["LabelValue09"]
      """  Value to display on package control label.  """  
      self.LabelValue10:str = obj["LabelValue10"]
      """  Value to display on package control label.  """  
      self.LabelValue11:str = obj["LabelValue11"]
      """  Value to display on package control label.  """  
      self.LabelValue12:str = obj["LabelValue12"]
      """  Value to display on package control label.  """  
      self.LabelValue13:str = obj["LabelValue13"]
      """  Value to display on package control label.  """  
      self.LabelValue14:str = obj["LabelValue14"]
      """  Value to display on package control label.  """  
      self.LabelValue15:str = obj["LabelValue15"]
      """  Value to display on package control label.  """  
      self.LabelValue16:str = obj["LabelValue16"]
      """  Value to display on package control label.  """  
      self.LabelValue17:str = obj["LabelValue17"]
      """  Value to display on package control label.  """  
      self.LabelValue18:str = obj["LabelValue18"]
      """  Value to display on package control label.  """  
      self.LabelValue19:str = obj["LabelValue19"]
      """  Value to display on package control label.  """  
      self.LabelValue20:str = obj["LabelValue20"]
      """  Value to display on package control label.  """  
      self.LabelValue21:str = obj["LabelValue21"]
      """  Value to display on package control label.  """  
      self.LabelValue22:str = obj["LabelValue22"]
      """  Value to display on package control label.  """  
      self.LabelValue23:str = obj["LabelValue23"]
      """  Value to display on package control label.  """  
      self.LabelValue24:str = obj["LabelValue24"]
      """  Value to display on package control label.  """  
      self.LabelValue25:str = obj["LabelValue25"]
      """  Value to display on package control label.  """  
      self.LabelValue26:str = obj["LabelValue26"]
      """  Value to display on package control label.  """  
      self.LabelValue27:str = obj["LabelValue27"]
      """  Value to display on package control label.  """  
      self.LabelValue28:str = obj["LabelValue28"]
      """  Value to display on package control label.  """  
      self.LabelValue29:str = obj["LabelValue29"]
      """  Value to display on package control label.  """  
      self.LabelValue30:str = obj["LabelValue30"]
      """  Value to display on package control label.  """  
      self.PkgControlCharacter01:str = obj["PkgControlCharacter01"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter02:str = obj["PkgControlCharacter02"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter03:str = obj["PkgControlCharacter03"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter04:str = obj["PkgControlCharacter04"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter05:str = obj["PkgControlCharacter05"]
      """  Reserved for development use.  """  
      self.PkgControlDate01:str = obj["PkgControlDate01"]
      """  Reserved for development use.  """  
      self.PkgControlDate02:str = obj["PkgControlDate02"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean01:bool = obj["PkgControlBoolean01"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean02:bool = obj["PkgControlBoolean02"]
      """  Reserved for development use.  """  
      self.PkgControlInteger01:int = obj["PkgControlInteger01"]
      """  Reserved for development use.  """  
      self.PkgControlInteger02:int = obj["PkgControlInteger02"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal01:int = obj["PkgControlDecimal01"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal02:int = obj["PkgControlDecimal02"]
      """  Reserved for development use.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.ExternalLength:int = obj["ExternalLength"]
      """  External Length dimension.  """  
      self.ExternalWidth:int = obj["ExternalWidth"]
      """  External Width dimension.  """  
      self.ExternalHeight:int = obj["ExternalHeight"]
      """  External Height dimension.  """  
      self.ExternalVolume:int = obj["ExternalVolume"]
      """  External Volume.  """  
      self.TareWeight:int = obj["TareWeight"]
      """  Tare Weight.  """  
      self.LabelPrintCount:int = obj["LabelPrintCount"]
      """  Incremental tally of number of times PCID label has been printed.  """  
      self.TrackExpendable:bool = obj["TrackExpendable"]
      """  Indicates if the expendable PCID will be tracked.  """  
      self.TrackReturnable:bool = obj["TrackReturnable"]
      """  Indicates if the returnable PCID will be tracked.  """  
      self.LabelType:str = obj["LabelType"]
      """  Label Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustNum:int = obj["CustNum"]
      """  Ship To Customer Number.  """  
      self.ContainerExpendable:bool = obj["ContainerExpendable"]
      """  Indicates if the PCID is expendable.  """  
      self.CustID:str = obj["CustID"]
      """  Ship To Customer ID.  """  
      self.CustName:str = obj["CustName"]
      """  Ship To Customer Name.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor Name.  """  
      self.VendorPPName:str = obj["VendorPPName"]
      """  Vendor Purchase Point Name.  """  
      self.AdhocStagedInventory:bool = obj["AdhocStagedInventory"]
      """  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  """  
      self.UpdatedByEmpID:str = obj["UpdatedByEmpID"]
      """  UpdatedByEmpID  """  
      self.RawBarcodeScan:str = obj["RawBarcodeScan"]
      """  Raw Barcode Scan prior to execution of any extract logic.  """  
      self.OutboundContainer:bool = obj["OutboundContainer"]
      """  OutboundContainer  """  
      self.BeforePackPkgControlStatus:str = obj["BeforePackPkgControlStatus"]
      """  PkgControlStatus value prior to being added to a pack.  """  
      self.BeforePackLabelPrintControlStatus:str = obj["BeforePackLabelPrintControlStatus"]
      """  LabelPrintControlStatus value prior to being added to a pack.  """  
      self.PackedFromSource:str = obj["PackedFromSource"]
      """  To indicate the source process when a PCID was added to a pack.  """  
      self.LastCountedDate:str = obj["LastCountedDate"]
      """  Date last counted.  Updated during the cycle count Posting Process.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  TFPackNum  """  
      self.ChildPCIDCount:int = obj["ChildPCIDCount"]
      """  Child PCID count  """  
      self.EnableCboReasonCode:bool = obj["EnableCboReasonCode"]
      """  Indicates if EnableCboReasonCode control should be Enabled.  """  
      self.Expendable:bool = obj["Expendable"]
      """  if the PkgControlID is expendable  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      self.HHASN:bool = obj["HHASN"]
      """  Used for Handheld, this field will determine if the ASN (Advanced Ship Notice) has been sent/printed  """  
      self.HHItemIUM:str = obj["HHItemIUM"]
      self.HHItemPartNum:str = obj["HHItemPartNum"]
      self.HHItemQuantity:int = obj["HHItemQuantity"]
      """  Used for Handheld.  """  
      self.HHItemRevisionNum:str = obj["HHItemRevisionNum"]
      self.HHLabelStatus:str = obj["HHLabelStatus"]
      """  Used for HandHeld, it can be either PkgControlHeader.LabelPrintControlStatus OR PkgControlHeader.PkgControlStatus  """  
      self.HHPackSlip:int = obj["HHPackSlip"]
      """   Used for handHeld             
If PkgControlHeader.PkgControlType = Static then PkgControlHeader.PackNum
If PkgControlHeader.PkgControlType = Dynamic then PkgControlItem.PackNum  """  
      self.HHPackSlipList:str = obj["HHPackSlipList"]
      """  Used for HandHeld, It could contains a list of PackNum from the children  """  
      self.LWHDimUOM:str = obj["LWHDimUOM"]
      self.ParentBinNum:str = obj["ParentBinNum"]
      """  Warehouse Bin where the Parent PCID is currently located.  """  
      self.ParentCreatedDate:str = obj["ParentCreatedDate"]
      """  System date and time when the row was created.  """  
      self.ParentCustContainerPartNum:str = obj["ParentCustContainerPartNum"]
      """  Ship To Customer Container Part Number.  """  
      self.ParentCustID:str = obj["ParentCustID"]
      """  Parent Ship To Customer ID.  """  
      self.ParentLabelPrintControlled:bool = obj["ParentLabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.ParentLabelPrintControlStatus:str = obj["ParentLabelPrintControlStatus"]
      """  Label Print Control status.  """  
      self.ParentLabelType:str = obj["ParentLabelType"]
      """  Label Type.  """  
      self.ParentNumberOfPCIDs:int = obj["ParentNumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.ParentPackNum:int = obj["ParentPackNum"]
      """  Pack Number if applicable.  """  
      self.ParentPCID:str = obj["ParentPCID"]
      """  Parent Package Control Identification Number  """  
      self.ParentPkgCode:str = obj["ParentPkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.ParentPkgCodePartNum:str = obj["ParentPkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.ParentPkgControlStatus:str = obj["ParentPkgControlStatus"]
      """  PCID current status.  """  
      self.ParentPkgControlType:str = obj["ParentPkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.ParentPlant:str = obj["ParentPlant"]
      """  Site where the Parent PCID is currently located.  """  
      self.ParentPlantName:str = obj["ParentPlantName"]
      """  Site Name.  """  
      self.ParentShipToNum:str = obj["ParentShipToNum"]
      """  Parent Ship To Number.  """  
      self.ParentWarehouseCode:str = obj["ParentWarehouseCode"]
      """  Warehouse where the Parent PCID is currently located.  """  
      self.ParentWhseDesc:str = obj["ParentWhseDesc"]
      self.PartDesc:str = obj["PartDesc"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgType:str = obj["PkgType"]
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason Code  """  
      self.ResCodeIn:str = obj["ResCodeIn"]
      self.ResCodeOut:str = obj["ResCodeOut"]
      self.RTWhseDesc:str = obj["RTWhseDesc"]
      self.ShipToContainerPartID:str = obj["ShipToContainerPartID"]
      """  Ship To Container Part ID  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type  """  
      self.WhseDesc:str = obj["WhseDesc"]
      self.AdjustInventory:bool = obj["AdjustInventory"]
      """  Adjust Inventory  """  
      self.ContainerUOM:str = obj["ContainerUOM"]
      """  Container UOM  """  
      self.DisableReasonCode:bool = obj["DisableReasonCode"]
      self.EnableBtnVoidPCIDInv:bool = obj["EnableBtnVoidPCIDInv"]
      """  Indicates if BtnVoidPCIDInv control should be Enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinDescription:str = obj["BinDescription"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      """  PCID Item Sequence  """  
      self.ItemPCID:str = obj["ItemPCID"]
      """  The PCID of the item in this PCID.  """  
      self.ItemPartNum:str = obj["ItemPartNum"]
      """  The Part Number of the item in this PCID.  """  
      self.ItemRevisionNum:str = obj["ItemRevisionNum"]
      """  The Revision Number of the item in this PCID.  """  
      self.ItemPartDesc:str = obj["ItemPartDesc"]
      """  The Part Description of the item in this PCID.  """  
      self.ItemLotNum:str = obj["ItemLotNum"]
      """  The Lot Number of the item in this PCID.  """  
      self.ItemIUM:str = obj["ItemIUM"]
      """  The Inventory UOM of the item in this PCID.  """  
      self.ItemQuantity:int = obj["ItemQuantity"]
      """  The Quantity of the item in this PCID.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DemandType:str = obj["DemandType"]
      """  Demand Type.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number of the demand.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line Number of the demand.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order Release Number of the demand.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the demand.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence Number of the demand.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Sequence Number of the demand.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order Number of the demand.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line of the demand.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack Number if applicable.  """  
      self.PackLine:int = obj["PackLine"]
      """  Pack Line Number if applicable.  """  
      self.CustPartNum:str = obj["CustPartNum"]
      """  Ship To Customer Part Number.  """  
      self.CustPartRev:str = obj["CustPartRev"]
      """  Ship To Customer Part Revision.  """  
      self.CustPONum:str = obj["CustPONum"]
      """  The PO number that these parts were created against.  """  
      self.CustShipToEngineerAlert:str = obj["CustShipToEngineerAlert"]
      """  Engineering Alert to display on the label.  """  
      self.SafetyIndicator:bool = obj["SafetyIndicator"]
      """  Safety Indicator to display on the label.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.VendorPOType:str = obj["VendorPOType"]
      """  Purchase Order Type.  """  
      self.VendorPONum:int = obj["VendorPONum"]
      """  Purchase Order Number.  """  
      self.VendorPOLine:int = obj["VendorPOLine"]
      """  Purchase Order Line Number.  """  
      self.VendorPORelNum:int = obj["VendorPORelNum"]
      """  Purchase Order Release Number.  """  
      self.VendorPartNum:str = obj["VendorPartNum"]
      """  Supplier Part Number.  """  
      self.VendorUOM:str = obj["VendorUOM"]
      """  Supplier Unit of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Supplier Quantity.  """  
      self.ReceiptPackSlip:str = obj["ReceiptPackSlip"]
      """  Receipt Packing Slip.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  Receipt Type.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt Date.  """  
      self.ReceiptUOM:str = obj["ReceiptUOM"]
      """  Receipt UOM.  """  
      self.ReceiptQty:int = obj["ReceiptQty"]
      """  Receipt Quantity.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number.  """  
      self.RMALine:int = obj["RMALine"]
      """  RMA Line.  """  
      self.PkgControlCharacter01:str = obj["PkgControlCharacter01"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter02:str = obj["PkgControlCharacter02"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter03:str = obj["PkgControlCharacter03"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter04:str = obj["PkgControlCharacter04"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter05:str = obj["PkgControlCharacter05"]
      """  Reserved for development use.  """  
      self.PkgControlDate01:str = obj["PkgControlDate01"]
      """  Reserved for development use.  """  
      self.PkgControlDate02:str = obj["PkgControlDate02"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean01:bool = obj["PkgControlBoolean01"]
      """  Reserved for development  """  
      self.PkgControlBoolean02:bool = obj["PkgControlBoolean02"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal01:int = obj["PkgControlDecimal01"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal02:int = obj["PkgControlDecimal02"]
      """  Reserved for development use.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ShipmentInvoicedPosted:str = obj["ShipmentInvoicedPosted"]
      """  Set to INVOICED when invoice created, set to POSTED when invoice is posted.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  The job number on which the quantity on this record were produced  """  
      self.ItemAttributeSetID:int = obj["ItemAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  TFPackNum  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  TFPackLine  """  
      self.ItemPicked:bool = obj["ItemPicked"]
      """  Set to true if this PkgControlItem record was created by processing a mtl queue picking record  """  
      self.ItemPartWipSysRowID:str = obj["ItemPartWipSysRowID"]
      """  SysRowID of the PartWip to which this item relates. The value is a GUID.  If the item is not WIP, this column is blank.  This value should only ever be populated in a Staging or History PCID, never an Inventory PCID.  """  
      self.TrackType:str = obj["TrackType"]
      """  Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.  "R" - Raw Material a part which was issued to the job.  "M" - Manufactured Part. The part that is being manufactured.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job operation sequence number that part is related to.  """  
      self.InNonConformance:bool = obj["InNonConformance"]
      """  Indicates if the WIP has been sent to Non-Conformance.  """  
      self.InDMRProcessing:bool = obj["InDMRProcessing"]
      """  Indicates if the WIP has failed Non-Conformance and has been moved to DMR Processing.  """  
      self.ChildPCIDOrPart:str = obj["ChildPCIDOrPart"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.PackageCode:str = obj["PackageCode"]
      self.PlantName:str = obj["PlantName"]
      """  Site Name.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.WhseDesc:str = obj["WhseDesc"]
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.ItemAttributeSetDescription:str = obj["ItemAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.ItemAttributeSetShortDescription:str = obj["ItemAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ItemPartAttrClassID:str = obj["ItemPartAttrClassID"]
      self.ItemType:str = obj["ItemType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   pcID
   """  
   def __init__(self, obj):
      self.pcID:str = obj["pcID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PkgControlHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.Plant:str = obj["Plant"]
      """  Site where the PCID is currently located.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.ReturnToWarehouseCode:str = obj["ReturnToWarehouseCode"]
      """  Warehouse where the PCID return stock needs to be returned to.  """  
      self.ReturnToBinNum:str = obj["ReturnToBinNum"]
      """  Warehouse Bin where the PCID return stock needs to be returned to.  """  
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      """  PCID current status.  """  
      self.PkgControlPriorStatus:str = obj["PkgControlPriorStatus"]
      """  PCID prior status.  """  
      self.LabelPrintControlStatus:str = obj["LabelPrintControlStatus"]
      """  Label Print Control status.  """  
      self.LabelPrintControlPriorStatus:str = obj["LabelPrintControlPriorStatus"]
      """  Label Print Control prior status.  """  
      self.AllowParentPCID:bool = obj["AllowParentPCID"]
      """  If false then PCID is a single-level PCID that cannot be associated with a Parent.  """  
      self.AllowMixedParts:bool = obj["AllowMixedParts"]
      """  If false then PCID must contain only one PartNum.  """  
      self.AllowMixedLots:bool = obj["AllowMixedLots"]
      """  If false then PCID must contain only one LotNum for each Part on the PCID.  """  
      self.AllowMixedUOMs:bool = obj["AllowMixedUOMs"]
      """  If false then PCID must contain only one UOM per Part on the PCID.  """  
      self.AllowMixedChildPCIDs:bool = obj["AllowMixedChildPCIDs"]
      """  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  """  
      self.AllowMultipleSerialNumPerPCID:bool = obj["AllowMultipleSerialNumPerPCID"]
      """  If false then PCID must contain only one Serial Number per PCID.  """  
      self.LabelPrintControlled:bool = obj["LabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.LabelPrintCounter:bool = obj["LabelPrintCounter"]
      """  If false then the number of PCID label prints will not be tracked.  """  
      self.AllowVoids:bool = obj["AllowVoids"]
      """  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  """  
      self.AllowDeletes:bool = obj["AllowDeletes"]
      """  If false then PkgControlHeader and PkgControlItem cannot be deleted.  """  
      self.ArchivePCIDHistory:bool = obj["ArchivePCIDHistory"]
      """  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.LWHDimensionUOM:str = obj["LWHDimensionUOM"]
      """  User defined code which uniquely identifies the UOM for length, width, and height.  """  
      self.Length:int = obj["Length"]
      """  Length dimension.  """  
      self.Width:int = obj["Width"]
      """  Width dimension.  """  
      self.Height:int = obj["Height"]
      """  Height dimension.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """  User defined code which uniquely identifies the UOM for volume.  """  
      self.Volume:int = obj["Volume"]
      """  Volume.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  User defined code which uniquely identifies the UOM for weight.  """  
      self.MaximumWeight:int = obj["MaximumWeight"]
      """  Maximum Weight.  """  
      self.CalculatedWeight:int = obj["CalculatedWeight"]
      """  Calculated Weight.  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  The total weight of the parts and the container combined.  """  
      self.MaximumStack:int = obj["MaximumStack"]
      """  Maximum number of PCIDs allowed if vertically stacked.  """  
      self.PositionSeq:int = obj["PositionSeq"]
      """  Position Sequence within a parent PCID.  """  
      self.TrailerID:str = obj["TrailerID"]
      """  Trailer ID.  """  
      self.SecuritySealID:str = obj["SecuritySealID"]
      """  Bond or Security Seal ID.  """  
      self.RawPCIDLicensePlate:str = obj["RawPCIDLicensePlate"]
      """  Raw PCID as scanned or generated.  """  
      self.GS1128:str = obj["GS1128"]
      """  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  """  
      self.PkgControlCollapseCounter:int = obj["PkgControlCollapseCounter"]
      """  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  System date and time when the row was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this row.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  System date and time when the row was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID that last updated this row.  """  
      self.LastPCIDScanned:str = obj["LastPCIDScanned"]
      """  Last PCID Scanned.  """  
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.AutoPrint:bool = obj["AutoPrint"]
      """  Flag used to fire the auto print rule that will print the labels.  """  
      self.LPCCreatedDate:str = obj["LPCCreatedDate"]
      """  System date and time when the row was created.  """  
      self.LPCCreatedBy:str = obj["LPCCreatedBy"]
      """  The user ID that created this record.  """  
      self.LPCPrinterID:str = obj["LPCPrinterID"]
      """  Printer ID that printed the label.  """  
      self.LPCPrintedBy:str = obj["LPCPrintedBy"]
      """  User that printed the label.  """  
      self.LPCPrintedFromTx:str = obj["LPCPrintedFromTx"]
      """  Label feature. Displays what transaction the label was printed from.  """  
      self.LPCPrintedFromTxType:str = obj["LPCPrintedFromTxType"]
      """  Ad Hoc feature. Displays what transaction type the label was printed from.  """  
      self.LPCJobNum:str = obj["LPCJobNum"]
      """  The job for which the label was printed.  """  
      self.LPCOprSeq:int = obj["LPCOprSeq"]
      """  The operation sequence for which the label was printed.  """  
      self.LPCAssemblySeq:int = obj["LPCAssemblySeq"]
      """  The assembly sequence for which the label was printed.  """  
      self.LPCShift:int = obj["LPCShift"]
      """  Shift that the label was created on or shift entered in Ad Hoc print program.  """  
      self.LPCOperatorEmpID:str = obj["LPCOperatorEmpID"]
      """  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  """  
      self.OriginalSourcePCID:str = obj["OriginalSourcePCID"]
      """  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  """  
      self.OverlaidByPCID:str = obj["OverlaidByPCID"]
      """  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  """  
      self.Overlaid:bool = obj["Overlaid"]
      """  Set to True when PCID has been overlaid using the overlay feature.  """  
      self.ContainerPartial:bool = obj["ContainerPartial"]
      """  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  """  
      self.ContainerRepacked:bool = obj["ContainerRepacked"]
      """  If true the container was repacked.  """  
      self.ContainerReturnable:bool = obj["ContainerReturnable"]
      """  If true the container used is a returnable container.  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Vendor ID for the Customer being Shipped To.  """  
      self.PlantName:str = obj["PlantName"]
      """  Site Name.  """  
      self.PlantAddress1:str = obj["PlantAddress1"]
      """  Site Address line 1.  """  
      self.PlantAddress2:str = obj["PlantAddress2"]
      """  Site Address line 2.  """  
      self.PlantAddress3:str = obj["PlantAddress3"]
      """  Site Address line 3.  """  
      self.PlantCity:str = obj["PlantCity"]
      """  Site City.  """  
      self.PlantState:str = obj["PlantState"]
      """  Site State.  """  
      self.PlantZip:str = obj["PlantZip"]
      """  Site Zip.  """  
      self.PlantCountryNum:int = obj["PlantCountryNum"]
      """  Site Country Number.  """  
      self.PlantCountryDesc:str = obj["PlantCountryDesc"]
      """  Site Country Description.  """  
      self.PlantPhone:str = obj["PlantPhone"]
      """  Site Phone.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack Number if applicable.  """  
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      """  Ship To Customer Container Part Number.  """  
      self.EDIShipToNum:str = obj["EDIShipToNum"]
      """  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Ship To Number.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Name of the Ship To that the PCID is going to.  """  
      self.ShipToAddress1:str = obj["ShipToAddress1"]
      """  Address line 1 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress2:str = obj["ShipToAddress2"]
      """  Address line 2 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress3:str = obj["ShipToAddress3"]
      """  Address line 3 of the Ship To that the PCID is going to.  """  
      self.ShipToCity:str = obj["ShipToCity"]
      """  City of the Ship To that the PCID is going to.  """  
      self.ShipToState:str = obj["ShipToState"]
      """  State of the Ship To that the PCID is going to.  """  
      self.ShipToZip:str = obj["ShipToZip"]
      """  Zip of the Ship To that the PCID is going to.  """  
      self.ShipToCountryNum:int = obj["ShipToCountryNum"]
      """  Country number of the Ship To that the PCID is going to.  """  
      self.ShipToCountryDesc:str = obj["ShipToCountryDesc"]
      """  Country of the Ship To that the PCID is going to.  """  
      self.ShipToDock:str = obj["ShipToDock"]
      """  The dock that the parts should be shipped to.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID.  """  
      self.VendorPurPoint:str = obj["VendorPurPoint"]
      """  Vendor Purchase Point.  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  Vendor Address line 1.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Vendor Address line 2.  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Vendor Address line 3.  """  
      self.VendorCity:str = obj["VendorCity"]
      """  Vendor City.  """  
      self.VendorState:str = obj["VendorState"]
      """  Vendor State.  """  
      self.VendorZip:str = obj["VendorZip"]
      """  Vendor Zip.  """  
      self.VendorCountryNum:int = obj["VendorCountryNum"]
      """  Vendor Country Number.  """  
      self.VendorCountryDesc:str = obj["VendorCountryDesc"]
      """  Vendor Country Description.  """  
      self.OurDock:str = obj["OurDock"]
      """  Our Dock ID.  """  
      self.LabelValue01:str = obj["LabelValue01"]
      """  Value to display on package control label.  """  
      self.LabelValue02:str = obj["LabelValue02"]
      """  Value to display on package control label.  """  
      self.LabelValue03:str = obj["LabelValue03"]
      """  Value to display on package control label.  """  
      self.LabelValue04:str = obj["LabelValue04"]
      """  Value to display on package control label.  """  
      self.LabelValue05:str = obj["LabelValue05"]
      """  Value to display on package control label.  """  
      self.LabelValue06:str = obj["LabelValue06"]
      """  Value to display on package control label.  """  
      self.LabelValue07:str = obj["LabelValue07"]
      """  Value to display on package control label.  """  
      self.LabelValue08:str = obj["LabelValue08"]
      """  Value to display on package control label.  """  
      self.LabelValue09:str = obj["LabelValue09"]
      """  Value to display on package control label.  """  
      self.LabelValue10:str = obj["LabelValue10"]
      """  Value to display on package control label.  """  
      self.LabelValue11:str = obj["LabelValue11"]
      """  Value to display on package control label.  """  
      self.LabelValue12:str = obj["LabelValue12"]
      """  Value to display on package control label.  """  
      self.LabelValue13:str = obj["LabelValue13"]
      """  Value to display on package control label.  """  
      self.LabelValue14:str = obj["LabelValue14"]
      """  Value to display on package control label.  """  
      self.LabelValue15:str = obj["LabelValue15"]
      """  Value to display on package control label.  """  
      self.LabelValue16:str = obj["LabelValue16"]
      """  Value to display on package control label.  """  
      self.LabelValue17:str = obj["LabelValue17"]
      """  Value to display on package control label.  """  
      self.LabelValue18:str = obj["LabelValue18"]
      """  Value to display on package control label.  """  
      self.LabelValue19:str = obj["LabelValue19"]
      """  Value to display on package control label.  """  
      self.LabelValue20:str = obj["LabelValue20"]
      """  Value to display on package control label.  """  
      self.LabelValue21:str = obj["LabelValue21"]
      """  Value to display on package control label.  """  
      self.LabelValue22:str = obj["LabelValue22"]
      """  Value to display on package control label.  """  
      self.LabelValue23:str = obj["LabelValue23"]
      """  Value to display on package control label.  """  
      self.LabelValue24:str = obj["LabelValue24"]
      """  Value to display on package control label.  """  
      self.LabelValue25:str = obj["LabelValue25"]
      """  Value to display on package control label.  """  
      self.LabelValue26:str = obj["LabelValue26"]
      """  Value to display on package control label.  """  
      self.LabelValue27:str = obj["LabelValue27"]
      """  Value to display on package control label.  """  
      self.LabelValue28:str = obj["LabelValue28"]
      """  Value to display on package control label.  """  
      self.LabelValue29:str = obj["LabelValue29"]
      """  Value to display on package control label.  """  
      self.LabelValue30:str = obj["LabelValue30"]
      """  Value to display on package control label.  """  
      self.PkgControlCharacter01:str = obj["PkgControlCharacter01"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter02:str = obj["PkgControlCharacter02"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter03:str = obj["PkgControlCharacter03"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter04:str = obj["PkgControlCharacter04"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter05:str = obj["PkgControlCharacter05"]
      """  Reserved for development use.  """  
      self.PkgControlDate01:str = obj["PkgControlDate01"]
      """  Reserved for development use.  """  
      self.PkgControlDate02:str = obj["PkgControlDate02"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean01:bool = obj["PkgControlBoolean01"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean02:bool = obj["PkgControlBoolean02"]
      """  Reserved for development use.  """  
      self.PkgControlInteger01:int = obj["PkgControlInteger01"]
      """  Reserved for development use.  """  
      self.PkgControlInteger02:int = obj["PkgControlInteger02"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal01:int = obj["PkgControlDecimal01"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal02:int = obj["PkgControlDecimal02"]
      """  Reserved for development use.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.ExternalLength:int = obj["ExternalLength"]
      """  External Length dimension.  """  
      self.ExternalWidth:int = obj["ExternalWidth"]
      """  External Width dimension.  """  
      self.ExternalHeight:int = obj["ExternalHeight"]
      """  External Height dimension.  """  
      self.ExternalVolume:int = obj["ExternalVolume"]
      """  External Volume.  """  
      self.TareWeight:int = obj["TareWeight"]
      """  Tare Weight.  """  
      self.LabelPrintCount:int = obj["LabelPrintCount"]
      """  Incremental tally of number of times PCID label has been printed.  """  
      self.TrackExpendable:bool = obj["TrackExpendable"]
      """  Indicates if the expendable PCID will be tracked.  """  
      self.TrackReturnable:bool = obj["TrackReturnable"]
      """  Indicates if the returnable PCID will be tracked.  """  
      self.LabelType:str = obj["LabelType"]
      """  Label Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustNum:int = obj["CustNum"]
      """  Ship To Customer Number.  """  
      self.ContainerExpendable:bool = obj["ContainerExpendable"]
      """  Indicates if the PCID is expendable.  """  
      self.CustID:str = obj["CustID"]
      """  Ship To Customer ID.  """  
      self.CustName:str = obj["CustName"]
      """  Ship To Customer Name.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor Name.  """  
      self.VendorPPName:str = obj["VendorPPName"]
      """  Vendor Purchase Point Name.  """  
      self.AdhocStagedInventory:bool = obj["AdhocStagedInventory"]
      """  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  """  
      self.UpdatedByEmpID:str = obj["UpdatedByEmpID"]
      """  UpdatedByEmpID  """  
      self.RawBarcodeScan:str = obj["RawBarcodeScan"]
      """  Raw Barcode Scan prior to execution of any extract logic.  """  
      self.OutboundContainer:bool = obj["OutboundContainer"]
      """  OutboundContainer  """  
      self.BeforePackPkgControlStatus:str = obj["BeforePackPkgControlStatus"]
      """  PkgControlStatus value prior to being added to a pack.  """  
      self.BeforePackLabelPrintControlStatus:str = obj["BeforePackLabelPrintControlStatus"]
      """  LabelPrintControlStatus value prior to being added to a pack.  """  
      self.PackedFromSource:str = obj["PackedFromSource"]
      """  To indicate the source process when a PCID was added to a pack.  """  
      self.LastCountedDate:str = obj["LastCountedDate"]
      """  Date last counted.  Updated during the cycle count Posting Process.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  TFPackNum  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.Plant:str = obj["Plant"]
      """  Site where the PCID is currently located.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.ReturnToWarehouseCode:str = obj["ReturnToWarehouseCode"]
      """  Warehouse where the PCID return stock needs to be returned to.  """  
      self.ReturnToBinNum:str = obj["ReturnToBinNum"]
      """  Warehouse Bin where the PCID return stock needs to be returned to.  """  
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      """  PCID current status.  """  
      self.PkgControlPriorStatus:str = obj["PkgControlPriorStatus"]
      """  PCID prior status.  """  
      self.LabelPrintControlStatus:str = obj["LabelPrintControlStatus"]
      """  Label Print Control status.  """  
      self.LabelPrintControlPriorStatus:str = obj["LabelPrintControlPriorStatus"]
      """  Label Print Control prior status.  """  
      self.AllowParentPCID:bool = obj["AllowParentPCID"]
      """  If false then PCID is a single-level PCID that cannot be associated with a Parent.  """  
      self.AllowMixedParts:bool = obj["AllowMixedParts"]
      """  If false then PCID must contain only one PartNum.  """  
      self.AllowMixedLots:bool = obj["AllowMixedLots"]
      """  If false then PCID must contain only one LotNum for each Part on the PCID.  """  
      self.AllowMixedUOMs:bool = obj["AllowMixedUOMs"]
      """  If false then PCID must contain only one UOM per Part on the PCID.  """  
      self.AllowMixedChildPCIDs:bool = obj["AllowMixedChildPCIDs"]
      """  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  """  
      self.AllowMultipleSerialNumPerPCID:bool = obj["AllowMultipleSerialNumPerPCID"]
      """  If false then PCID must contain only one Serial Number per PCID.  """  
      self.LabelPrintControlled:bool = obj["LabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.LabelPrintCounter:bool = obj["LabelPrintCounter"]
      """  If false then the number of PCID label prints will not be tracked.  """  
      self.AllowVoids:bool = obj["AllowVoids"]
      """  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  """  
      self.AllowDeletes:bool = obj["AllowDeletes"]
      """  If false then PkgControlHeader and PkgControlItem cannot be deleted.  """  
      self.ArchivePCIDHistory:bool = obj["ArchivePCIDHistory"]
      """  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.LWHDimensionUOM:str = obj["LWHDimensionUOM"]
      """  User defined code which uniquely identifies the UOM for length, width, and height.  """  
      self.Length:int = obj["Length"]
      """  Length dimension.  """  
      self.Width:int = obj["Width"]
      """  Width dimension.  """  
      self.Height:int = obj["Height"]
      """  Height dimension.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """  User defined code which uniquely identifies the UOM for volume.  """  
      self.Volume:int = obj["Volume"]
      """  Volume.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  User defined code which uniquely identifies the UOM for weight.  """  
      self.MaximumWeight:int = obj["MaximumWeight"]
      """  Maximum Weight.  """  
      self.CalculatedWeight:int = obj["CalculatedWeight"]
      """  Calculated Weight.  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  The total weight of the parts and the container combined.  """  
      self.MaximumStack:int = obj["MaximumStack"]
      """  Maximum number of PCIDs allowed if vertically stacked.  """  
      self.PositionSeq:int = obj["PositionSeq"]
      """  Position Sequence within a parent PCID.  """  
      self.TrailerID:str = obj["TrailerID"]
      """  Trailer ID.  """  
      self.SecuritySealID:str = obj["SecuritySealID"]
      """  Bond or Security Seal ID.  """  
      self.RawPCIDLicensePlate:str = obj["RawPCIDLicensePlate"]
      """  Raw PCID as scanned or generated.  """  
      self.GS1128:str = obj["GS1128"]
      """  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  """  
      self.PkgControlCollapseCounter:int = obj["PkgControlCollapseCounter"]
      """  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  System date and time when the row was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this row.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  System date and time when the row was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID that last updated this row.  """  
      self.LastPCIDScanned:str = obj["LastPCIDScanned"]
      """  Last PCID Scanned.  """  
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.AutoPrint:bool = obj["AutoPrint"]
      """  Flag used to fire the auto print rule that will print the labels.  """  
      self.LPCCreatedDate:str = obj["LPCCreatedDate"]
      """  System date and time when the row was created.  """  
      self.LPCCreatedBy:str = obj["LPCCreatedBy"]
      """  The user ID that created this record.  """  
      self.LPCPrinterID:str = obj["LPCPrinterID"]
      """  Printer ID that printed the label.  """  
      self.LPCPrintedBy:str = obj["LPCPrintedBy"]
      """  User that printed the label.  """  
      self.LPCPrintedFromTx:str = obj["LPCPrintedFromTx"]
      """  Label feature. Displays what transaction the label was printed from.  """  
      self.LPCPrintedFromTxType:str = obj["LPCPrintedFromTxType"]
      """  Ad Hoc feature. Displays what transaction type the label was printed from.  """  
      self.LPCJobNum:str = obj["LPCJobNum"]
      """  The job for which the label was printed.  """  
      self.LPCOprSeq:int = obj["LPCOprSeq"]
      """  The operation sequence for which the label was printed.  """  
      self.LPCAssemblySeq:int = obj["LPCAssemblySeq"]
      """  The assembly sequence for which the label was printed.  """  
      self.LPCShift:int = obj["LPCShift"]
      """  Shift that the label was created on or shift entered in Ad Hoc print program.  """  
      self.LPCOperatorEmpID:str = obj["LPCOperatorEmpID"]
      """  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  """  
      self.OriginalSourcePCID:str = obj["OriginalSourcePCID"]
      """  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  """  
      self.OverlaidByPCID:str = obj["OverlaidByPCID"]
      """  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  """  
      self.Overlaid:bool = obj["Overlaid"]
      """  Set to True when PCID has been overlaid using the overlay feature.  """  
      self.ContainerPartial:bool = obj["ContainerPartial"]
      """  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  """  
      self.ContainerRepacked:bool = obj["ContainerRepacked"]
      """  If true the container was repacked.  """  
      self.ContainerReturnable:bool = obj["ContainerReturnable"]
      """  If true the container used is a returnable container.  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Vendor ID for the Customer being Shipped To.  """  
      self.PlantName:str = obj["PlantName"]
      """  Site Name.  """  
      self.PlantAddress1:str = obj["PlantAddress1"]
      """  Site Address line 1.  """  
      self.PlantAddress2:str = obj["PlantAddress2"]
      """  Site Address line 2.  """  
      self.PlantAddress3:str = obj["PlantAddress3"]
      """  Site Address line 3.  """  
      self.PlantCity:str = obj["PlantCity"]
      """  Site City.  """  
      self.PlantState:str = obj["PlantState"]
      """  Site State.  """  
      self.PlantZip:str = obj["PlantZip"]
      """  Site Zip.  """  
      self.PlantCountryNum:int = obj["PlantCountryNum"]
      """  Site Country Number.  """  
      self.PlantCountryDesc:str = obj["PlantCountryDesc"]
      """  Site Country Description.  """  
      self.PlantPhone:str = obj["PlantPhone"]
      """  Site Phone.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack Number if applicable.  """  
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      """  Ship To Customer Container Part Number.  """  
      self.EDIShipToNum:str = obj["EDIShipToNum"]
      """  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Ship To Number.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Name of the Ship To that the PCID is going to.  """  
      self.ShipToAddress1:str = obj["ShipToAddress1"]
      """  Address line 1 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress2:str = obj["ShipToAddress2"]
      """  Address line 2 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress3:str = obj["ShipToAddress3"]
      """  Address line 3 of the Ship To that the PCID is going to.  """  
      self.ShipToCity:str = obj["ShipToCity"]
      """  City of the Ship To that the PCID is going to.  """  
      self.ShipToState:str = obj["ShipToState"]
      """  State of the Ship To that the PCID is going to.  """  
      self.ShipToZip:str = obj["ShipToZip"]
      """  Zip of the Ship To that the PCID is going to.  """  
      self.ShipToCountryNum:int = obj["ShipToCountryNum"]
      """  Country number of the Ship To that the PCID is going to.  """  
      self.ShipToCountryDesc:str = obj["ShipToCountryDesc"]
      """  Country of the Ship To that the PCID is going to.  """  
      self.ShipToDock:str = obj["ShipToDock"]
      """  The dock that the parts should be shipped to.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID.  """  
      self.VendorPurPoint:str = obj["VendorPurPoint"]
      """  Vendor Purchase Point.  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  Vendor Address line 1.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Vendor Address line 2.  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Vendor Address line 3.  """  
      self.VendorCity:str = obj["VendorCity"]
      """  Vendor City.  """  
      self.VendorState:str = obj["VendorState"]
      """  Vendor State.  """  
      self.VendorZip:str = obj["VendorZip"]
      """  Vendor Zip.  """  
      self.VendorCountryNum:int = obj["VendorCountryNum"]
      """  Vendor Country Number.  """  
      self.VendorCountryDesc:str = obj["VendorCountryDesc"]
      """  Vendor Country Description.  """  
      self.OurDock:str = obj["OurDock"]
      """  Our Dock ID.  """  
      self.LabelValue01:str = obj["LabelValue01"]
      """  Value to display on package control label.  """  
      self.LabelValue02:str = obj["LabelValue02"]
      """  Value to display on package control label.  """  
      self.LabelValue03:str = obj["LabelValue03"]
      """  Value to display on package control label.  """  
      self.LabelValue04:str = obj["LabelValue04"]
      """  Value to display on package control label.  """  
      self.LabelValue05:str = obj["LabelValue05"]
      """  Value to display on package control label.  """  
      self.LabelValue06:str = obj["LabelValue06"]
      """  Value to display on package control label.  """  
      self.LabelValue07:str = obj["LabelValue07"]
      """  Value to display on package control label.  """  
      self.LabelValue08:str = obj["LabelValue08"]
      """  Value to display on package control label.  """  
      self.LabelValue09:str = obj["LabelValue09"]
      """  Value to display on package control label.  """  
      self.LabelValue10:str = obj["LabelValue10"]
      """  Value to display on package control label.  """  
      self.LabelValue11:str = obj["LabelValue11"]
      """  Value to display on package control label.  """  
      self.LabelValue12:str = obj["LabelValue12"]
      """  Value to display on package control label.  """  
      self.LabelValue13:str = obj["LabelValue13"]
      """  Value to display on package control label.  """  
      self.LabelValue14:str = obj["LabelValue14"]
      """  Value to display on package control label.  """  
      self.LabelValue15:str = obj["LabelValue15"]
      """  Value to display on package control label.  """  
      self.LabelValue16:str = obj["LabelValue16"]
      """  Value to display on package control label.  """  
      self.LabelValue17:str = obj["LabelValue17"]
      """  Value to display on package control label.  """  
      self.LabelValue18:str = obj["LabelValue18"]
      """  Value to display on package control label.  """  
      self.LabelValue19:str = obj["LabelValue19"]
      """  Value to display on package control label.  """  
      self.LabelValue20:str = obj["LabelValue20"]
      """  Value to display on package control label.  """  
      self.LabelValue21:str = obj["LabelValue21"]
      """  Value to display on package control label.  """  
      self.LabelValue22:str = obj["LabelValue22"]
      """  Value to display on package control label.  """  
      self.LabelValue23:str = obj["LabelValue23"]
      """  Value to display on package control label.  """  
      self.LabelValue24:str = obj["LabelValue24"]
      """  Value to display on package control label.  """  
      self.LabelValue25:str = obj["LabelValue25"]
      """  Value to display on package control label.  """  
      self.LabelValue26:str = obj["LabelValue26"]
      """  Value to display on package control label.  """  
      self.LabelValue27:str = obj["LabelValue27"]
      """  Value to display on package control label.  """  
      self.LabelValue28:str = obj["LabelValue28"]
      """  Value to display on package control label.  """  
      self.LabelValue29:str = obj["LabelValue29"]
      """  Value to display on package control label.  """  
      self.LabelValue30:str = obj["LabelValue30"]
      """  Value to display on package control label.  """  
      self.PkgControlCharacter01:str = obj["PkgControlCharacter01"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter02:str = obj["PkgControlCharacter02"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter03:str = obj["PkgControlCharacter03"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter04:str = obj["PkgControlCharacter04"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter05:str = obj["PkgControlCharacter05"]
      """  Reserved for development use.  """  
      self.PkgControlDate01:str = obj["PkgControlDate01"]
      """  Reserved for development use.  """  
      self.PkgControlDate02:str = obj["PkgControlDate02"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean01:bool = obj["PkgControlBoolean01"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean02:bool = obj["PkgControlBoolean02"]
      """  Reserved for development use.  """  
      self.PkgControlInteger01:int = obj["PkgControlInteger01"]
      """  Reserved for development use.  """  
      self.PkgControlInteger02:int = obj["PkgControlInteger02"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal01:int = obj["PkgControlDecimal01"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal02:int = obj["PkgControlDecimal02"]
      """  Reserved for development use.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.ExternalLength:int = obj["ExternalLength"]
      """  External Length dimension.  """  
      self.ExternalWidth:int = obj["ExternalWidth"]
      """  External Width dimension.  """  
      self.ExternalHeight:int = obj["ExternalHeight"]
      """  External Height dimension.  """  
      self.ExternalVolume:int = obj["ExternalVolume"]
      """  External Volume.  """  
      self.TareWeight:int = obj["TareWeight"]
      """  Tare Weight.  """  
      self.LabelPrintCount:int = obj["LabelPrintCount"]
      """  Incremental tally of number of times PCID label has been printed.  """  
      self.TrackExpendable:bool = obj["TrackExpendable"]
      """  Indicates if the expendable PCID will be tracked.  """  
      self.TrackReturnable:bool = obj["TrackReturnable"]
      """  Indicates if the returnable PCID will be tracked.  """  
      self.LabelType:str = obj["LabelType"]
      """  Label Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustNum:int = obj["CustNum"]
      """  Ship To Customer Number.  """  
      self.ContainerExpendable:bool = obj["ContainerExpendable"]
      """  Indicates if the PCID is expendable.  """  
      self.CustID:str = obj["CustID"]
      """  Ship To Customer ID.  """  
      self.CustName:str = obj["CustName"]
      """  Ship To Customer Name.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor Name.  """  
      self.VendorPPName:str = obj["VendorPPName"]
      """  Vendor Purchase Point Name.  """  
      self.AdhocStagedInventory:bool = obj["AdhocStagedInventory"]
      """  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  """  
      self.UpdatedByEmpID:str = obj["UpdatedByEmpID"]
      """  UpdatedByEmpID  """  
      self.RawBarcodeScan:str = obj["RawBarcodeScan"]
      """  Raw Barcode Scan prior to execution of any extract logic.  """  
      self.OutboundContainer:bool = obj["OutboundContainer"]
      """  OutboundContainer  """  
      self.BeforePackPkgControlStatus:str = obj["BeforePackPkgControlStatus"]
      """  PkgControlStatus value prior to being added to a pack.  """  
      self.BeforePackLabelPrintControlStatus:str = obj["BeforePackLabelPrintControlStatus"]
      """  LabelPrintControlStatus value prior to being added to a pack.  """  
      self.PackedFromSource:str = obj["PackedFromSource"]
      """  To indicate the source process when a PCID was added to a pack.  """  
      self.LastCountedDate:str = obj["LastCountedDate"]
      """  Date last counted.  Updated during the cycle count Posting Process.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  TFPackNum  """  
      self.ChildPCIDCount:int = obj["ChildPCIDCount"]
      """  Child PCID count  """  
      self.EnableCboReasonCode:bool = obj["EnableCboReasonCode"]
      """  Indicates if EnableCboReasonCode control should be Enabled.  """  
      self.Expendable:bool = obj["Expendable"]
      """  if the PkgControlID is expendable  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      self.HHASN:bool = obj["HHASN"]
      """  Used for Handheld, this field will determine if the ASN (Advanced Ship Notice) has been sent/printed  """  
      self.HHItemIUM:str = obj["HHItemIUM"]
      self.HHItemPartNum:str = obj["HHItemPartNum"]
      self.HHItemQuantity:int = obj["HHItemQuantity"]
      """  Used for Handheld.  """  
      self.HHItemRevisionNum:str = obj["HHItemRevisionNum"]
      self.HHLabelStatus:str = obj["HHLabelStatus"]
      """  Used for HandHeld, it can be either PkgControlHeader.LabelPrintControlStatus OR PkgControlHeader.PkgControlStatus  """  
      self.HHPackSlip:int = obj["HHPackSlip"]
      """   Used for handHeld             
If PkgControlHeader.PkgControlType = Static then PkgControlHeader.PackNum
If PkgControlHeader.PkgControlType = Dynamic then PkgControlItem.PackNum  """  
      self.HHPackSlipList:str = obj["HHPackSlipList"]
      """  Used for HandHeld, It could contains a list of PackNum from the children  """  
      self.LWHDimUOM:str = obj["LWHDimUOM"]
      self.ParentBinNum:str = obj["ParentBinNum"]
      """  Warehouse Bin where the Parent PCID is currently located.  """  
      self.ParentCreatedDate:str = obj["ParentCreatedDate"]
      """  System date and time when the row was created.  """  
      self.ParentCustContainerPartNum:str = obj["ParentCustContainerPartNum"]
      """  Ship To Customer Container Part Number.  """  
      self.ParentCustID:str = obj["ParentCustID"]
      """  Parent Ship To Customer ID.  """  
      self.ParentLabelPrintControlled:bool = obj["ParentLabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.ParentLabelPrintControlStatus:str = obj["ParentLabelPrintControlStatus"]
      """  Label Print Control status.  """  
      self.ParentLabelType:str = obj["ParentLabelType"]
      """  Label Type.  """  
      self.ParentNumberOfPCIDs:int = obj["ParentNumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.ParentPackNum:int = obj["ParentPackNum"]
      """  Pack Number if applicable.  """  
      self.ParentPCID:str = obj["ParentPCID"]
      """  Parent Package Control Identification Number  """  
      self.ParentPkgCode:str = obj["ParentPkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.ParentPkgCodePartNum:str = obj["ParentPkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.ParentPkgControlStatus:str = obj["ParentPkgControlStatus"]
      """  PCID current status.  """  
      self.ParentPkgControlType:str = obj["ParentPkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.ParentPlant:str = obj["ParentPlant"]
      """  Site where the Parent PCID is currently located.  """  
      self.ParentPlantName:str = obj["ParentPlantName"]
      """  Site Name.  """  
      self.ParentShipToNum:str = obj["ParentShipToNum"]
      """  Parent Ship To Number.  """  
      self.ParentWarehouseCode:str = obj["ParentWarehouseCode"]
      """  Warehouse where the Parent PCID is currently located.  """  
      self.ParentWhseDesc:str = obj["ParentWhseDesc"]
      self.PartDesc:str = obj["PartDesc"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgType:str = obj["PkgType"]
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason Code  """  
      self.ResCodeIn:str = obj["ResCodeIn"]
      self.ResCodeOut:str = obj["ResCodeOut"]
      self.RTWhseDesc:str = obj["RTWhseDesc"]
      self.ShipToContainerPartID:str = obj["ShipToContainerPartID"]
      """  Ship To Container Part ID  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type  """  
      self.WhseDesc:str = obj["WhseDesc"]
      self.AdjustInventory:bool = obj["AdjustInventory"]
      """  Adjust Inventory  """  
      self.ContainerUOM:str = obj["ContainerUOM"]
      """  Container UOM  """  
      self.DisableReasonCode:bool = obj["DisableReasonCode"]
      self.EnableBtnVoidPCIDInv:bool = obj["EnableBtnVoidPCIDInv"]
      """  Indicates if BtnVoidPCIDInv control should be Enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinDescription:str = obj["BinDescription"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      """  PCID Item Sequence  """  
      self.ItemPCID:str = obj["ItemPCID"]
      """  The PCID of the item in this PCID.  """  
      self.ItemPartNum:str = obj["ItemPartNum"]
      """  The Part Number of the item in this PCID.  """  
      self.ItemRevisionNum:str = obj["ItemRevisionNum"]
      """  The Revision Number of the item in this PCID.  """  
      self.ItemPartDesc:str = obj["ItemPartDesc"]
      """  The Part Description of the item in this PCID.  """  
      self.ItemLotNum:str = obj["ItemLotNum"]
      """  The Lot Number of the item in this PCID.  """  
      self.ItemIUM:str = obj["ItemIUM"]
      """  The Inventory UOM of the item in this PCID.  """  
      self.ItemQuantity:int = obj["ItemQuantity"]
      """  The Quantity of the item in this PCID.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DemandType:str = obj["DemandType"]
      """  Demand Type.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number of the demand.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line Number of the demand.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order Release Number of the demand.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the demand.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence Number of the demand.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Sequence Number of the demand.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order Number of the demand.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line of the demand.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack Number if applicable.  """  
      self.PackLine:int = obj["PackLine"]
      """  Pack Line Number if applicable.  """  
      self.CustPartNum:str = obj["CustPartNum"]
      """  Ship To Customer Part Number.  """  
      self.CustPartRev:str = obj["CustPartRev"]
      """  Ship To Customer Part Revision.  """  
      self.CustPONum:str = obj["CustPONum"]
      """  The PO number that these parts were created against.  """  
      self.CustShipToEngineerAlert:str = obj["CustShipToEngineerAlert"]
      """  Engineering Alert to display on the label.  """  
      self.SafetyIndicator:bool = obj["SafetyIndicator"]
      """  Safety Indicator to display on the label.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.VendorPOType:str = obj["VendorPOType"]
      """  Purchase Order Type.  """  
      self.VendorPONum:int = obj["VendorPONum"]
      """  Purchase Order Number.  """  
      self.VendorPOLine:int = obj["VendorPOLine"]
      """  Purchase Order Line Number.  """  
      self.VendorPORelNum:int = obj["VendorPORelNum"]
      """  Purchase Order Release Number.  """  
      self.VendorPartNum:str = obj["VendorPartNum"]
      """  Supplier Part Number.  """  
      self.VendorUOM:str = obj["VendorUOM"]
      """  Supplier Unit of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Supplier Quantity.  """  
      self.ReceiptPackSlip:str = obj["ReceiptPackSlip"]
      """  Receipt Packing Slip.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  Receipt Type.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt Date.  """  
      self.ReceiptUOM:str = obj["ReceiptUOM"]
      """  Receipt UOM.  """  
      self.ReceiptQty:int = obj["ReceiptQty"]
      """  Receipt Quantity.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number.  """  
      self.RMALine:int = obj["RMALine"]
      """  RMA Line.  """  
      self.PkgControlCharacter01:str = obj["PkgControlCharacter01"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter02:str = obj["PkgControlCharacter02"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter03:str = obj["PkgControlCharacter03"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter04:str = obj["PkgControlCharacter04"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter05:str = obj["PkgControlCharacter05"]
      """  Reserved for development use.  """  
      self.PkgControlDate01:str = obj["PkgControlDate01"]
      """  Reserved for development use.  """  
      self.PkgControlDate02:str = obj["PkgControlDate02"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean01:bool = obj["PkgControlBoolean01"]
      """  Reserved for development  """  
      self.PkgControlBoolean02:bool = obj["PkgControlBoolean02"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal01:int = obj["PkgControlDecimal01"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal02:int = obj["PkgControlDecimal02"]
      """  Reserved for development use.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ShipmentInvoicedPosted:str = obj["ShipmentInvoicedPosted"]
      """  Set to INVOICED when invoice created, set to POSTED when invoice is posted.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  The job number on which the quantity on this record were produced  """  
      self.ItemAttributeSetID:int = obj["ItemAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  TFPackNum  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  TFPackLine  """  
      self.ItemPicked:bool = obj["ItemPicked"]
      """  Set to true if this PkgControlItem record was created by processing a mtl queue picking record  """  
      self.ItemPartWipSysRowID:str = obj["ItemPartWipSysRowID"]
      """  SysRowID of the PartWip to which this item relates. The value is a GUID.  If the item is not WIP, this column is blank.  This value should only ever be populated in a Staging or History PCID, never an Inventory PCID.  """  
      self.TrackType:str = obj["TrackType"]
      """  Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.  "R" - Raw Material a part which was issued to the job.  "M" - Manufactured Part. The part that is being manufactured.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job operation sequence number that part is related to.  """  
      self.InNonConformance:bool = obj["InNonConformance"]
      """  Indicates if the WIP has been sent to Non-Conformance.  """  
      self.InDMRProcessing:bool = obj["InDMRProcessing"]
      """  Indicates if the WIP has failed Non-Conformance and has been moved to DMR Processing.  """  
      self.ChildPCIDOrPart:str = obj["ChildPCIDOrPart"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.PackageCode:str = obj["PackageCode"]
      self.PlantName:str = obj["PlantName"]
      """  Site Name.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.WhseDesc:str = obj["WhseDesc"]
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.ItemAttributeSetDescription:str = obj["ItemAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.ItemAttributeSetShortDescription:str = obj["ItemAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ItemPartAttrClassID:str = obj["ItemPartAttrClassID"]
      self.ItemType:str = obj["ItemType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgCtrlOverlayPCIDValidateListTableset:
   def __init__(self, obj):
      self.PkgControlHeaderList:list[Erp_Tablesets_PkgControlHeaderListRow] = obj["PkgControlHeaderList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset:
   def __init__(self, obj):
      self.PkgControlHeader:list[Erp_Tablesets_PkgControlHeaderRow] = obj["PkgControlHeader"]
      self.PkgControlItem:list[Erp_Tablesets_PkgControlItemRow] = obj["PkgControlItem"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPkgCtrlOverlayPCIDValidateTableset:
   def __init__(self, obj):
      self.PkgControlHeader:list[Erp_Tablesets_PkgControlHeaderRow] = obj["PkgControlHeader"]
      self.PkgControlItem:list[Erp_Tablesets_PkgControlItemRow] = obj["PkgControlItem"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   pcID
   """  
   def __init__(self, obj):
      self.pcID:str = obj["pcID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPkgControlHeader_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["ds"]
      pass

class GetNewPkgControlHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPkgControlItem_input:
   """ Required : 
   ds
   pcID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["ds"]
      self.pcID:str = obj["pcID"]
      pass

class GetNewPkgControlItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePkgControlHeader
   whereClausePkgControlItem
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePkgControlHeader:str = obj["whereClausePkgControlHeader"]
      self.whereClausePkgControlItem:str = obj["whereClausePkgControlItem"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["returnObj"]
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

class OverlayPCIDValidationProcess_input:
   """ Required : 
   pcid
   overlay
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      self.overlay:str = obj["overlay"]
      pass

class OverlayPCIDValidationProcess_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgCtrlOverlayPCIDValidateTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgCtrlOverlayPCIDValidateTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOverlayPCID_input:
   """ Required : 
   pcid
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      pass

class ValidateOverlayPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["returnObj"]
      pass

class ValidatePCID_input:
   """ Required : 
   pcid
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      pass

class ValidatePCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgCtrlOverlayPCIDValidateTableset] = obj["returnObj"]
      pass

