import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.UOMClassSvc
# Description: UOM class BL
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_UOMClasses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UOMClasses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UOMClasses
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UOMClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses",headers=creds) as resp:
           return await resp.json()

async def post_UOMClasses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UOMClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UOMClassRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.UOMClassRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UOMClasses_Company_UOMClassID(Company, UOMClassID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UOMClass item
   Description: Calls GetByID to retrieve the UOMClass item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UOMClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UOMClassID: Desc: UOMClassID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UOMClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UOMClasses_Company_UOMClassID(Company, UOMClassID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UOMClass for the service
   Description: Calls UpdateExt to update UOMClass. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UOMClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UOMClassID: Desc: UOMClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.UOMClassRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UOMClasses_Company_UOMClassID(Company, UOMClassID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UOMClass item
   Description: Call UpdateExt to delete UOMClass item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UOMClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UOMClassID: Desc: UOMClassID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")",headers=creds) as resp:
           return await resp.json()

async def get_UOMClasses_Company_UOMClassID_UOMConvs(Company, UOMClassID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get UOMConvs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UOMConvs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UOMClassID: Desc: UOMClassID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UOMConvRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")/UOMConvs",headers=creds) as resp:
           return await resp.json()

async def get_UOMClasses_Company_UOMClassID_UOMConvs_Company_UOMClassID_UOMCode(Company, UOMClassID, UOMCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UOMConv item
   Description: Calls GetByID to retrieve the UOMConv item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UOMConv1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UOMClassID: Desc: UOMClassID   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UOMConvRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMClasses(" + Company + "," + UOMClassID + ")/UOMConvs(" + Company + "," + UOMClassID + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_UOMConvs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UOMConvs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UOMConvs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UOMConvRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs",headers=creds) as resp:
           return await resp.json()

async def post_UOMConvs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UOMConvs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UOMConvRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.UOMConvRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UOMConvs_Company_UOMClassID_UOMCode(Company, UOMClassID, UOMCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UOMConv item
   Description: Calls GetByID to retrieve the UOMConv item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UOMConv
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UOMClassID: Desc: UOMClassID   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UOMConvRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs(" + Company + "," + UOMClassID + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UOMConvs_Company_UOMClassID_UOMCode(Company, UOMClassID, UOMCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UOMConv for the service
   Description: Calls UpdateExt to update UOMConv. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UOMConv
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UOMClassID: Desc: UOMClassID   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.UOMConvRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs(" + Company + "," + UOMClassID + "," + UOMCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UOMConvs_Company_UOMClassID_UOMCode(Company, UOMClassID, UOMCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UOMConv item
   Description: Call UpdateExt to delete UOMConv item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UOMConv
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UOMClassID: Desc: UOMClassID   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/UOMConvs(" + Company + "," + UOMClassID + "," + UOMCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UOMClassListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseUOMClass, whereClauseUOMConv, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseUOMClass=" + whereClauseUOMClass
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUOMConv=" + whereClauseUOMConv
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(uoMClassID, epicorHeaders = None):
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
   params += "uoMClassID=" + uoMClassID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAllowDecimal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAllowDecimal
   Description: This method should be called when AllowDecimal changes.
   OperationID: OnChangeAllowDecimal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAllowDecimal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAllowDecimal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBaseUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBaseUOM
   Description: This method should be called when Base UOM changes.
   OperationID: OnChangeBaseUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBaseUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBaseUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeClassType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeClassType
   Description: This method should be called when the ClassType changes.
   OperationID: OnChangeClassType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeClassType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeClassType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDispPkgDisplaySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDispPkgDisplaySeq
   Description: This method should be called when UOMConv PkgCode changes.
   OperationID: OnChangeDispPkgDisplaySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDispPkgDisplaySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDispPkgDisplaySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePkgCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePkgCode
   Description: This method should be called when UOMConv PkgCode changes.
   OperationID: OnChangePkgCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUOMCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUOMCode
   Description: Called when the UOMCode is changed when creating a new UOMConv Record.
Refreshes UOMConv.UOMDesc UOMSymbol AllowDecimals NumOfDec Rounding
   OperationID: OnChangeUOMCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUOMCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOMCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: An override to the standard GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateUOMClassId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateUOMClassId
   Description: Called when the UOMClassId is changed when creating a new UOMClassId Record.
   OperationID: ValidateUOMClassId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUOMClassId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUOMClassId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUOMClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUOMClass
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUOMClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUOMClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUOMClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUOMConv(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUOMConv
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUOMConv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUOMConv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUOMConv_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UOMClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMClassListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UOMClassListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMClassRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UOMClassRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UOMConvRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UOMConvRow] = obj["value"]
      pass

class Erp_Tablesets_UOMClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  Unit of Measure Class Identifier.  User defined. Mandatory. Unique key component. Examples: Length, Volume, Weight,Roll,Bar,Sheet  """  
      self.Description:str = obj["Description"]
      """  A decription for the UOMClass.  Mandatory.  """  
      self.ClassType:str = obj["ClassType"]
      """   defines the type of class. Valid values are; Length,Area,Weight,Volume,Count or Other  All except "Other" are considered standard types.  There can be only 1 uom class per standard class type.
Having a ClassType allows the system to filter the  list of uoms when only a certain type is the only logical choice. Such as the case when entering the length, width, height of a bin. In this case the only logical choice would be the UOMs that belong to the "Length" class.  """  
      self.BaseUOMCode:str = obj["BaseUOMCode"]
      """  Base Unit of Measure for the class. Mandatory to perfrom UOM conversions. Must be valid in UOMConv table of the UOMClass. The initial UOMConv record created will be set as the BaseUOM. The User will be able to change this if they need to once other UOMConv records are created.  BaseUOM  is the reference point for establishing conversion factors of the other uoms within the class (see UOMConv definitions). It always has a conversion factor of 1. Normally this is the smallest unit that you wish considered.  """  
      self.DefUomCode:str = obj["DefUomCode"]
      """   Indicates which UOM of the class should be used as the default when creating new parts using this class. Optional.
This replaces the 8.3 logic which used XASyst.DefaultUOM. (See also XASyst.DefUOMClassID)  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the UOMClass is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  """  
      self.GlobalUOMClass:bool = obj["GlobalUOMClass"]
      """  Marks this UOMClass as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultUOMClass:bool = obj["DefaultUOMClass"]
      """  Signifies this is the Default UOM Class.  This is stored in XASyst.DefUOMClassID.  Used as a default value when creating new Part masters.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UOMClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  Unit of Measure Class Identifier.  User defined. Mandatory. Unique key component. Examples: Length, Volume, Weight,Roll,Bar,Sheet  """  
      self.Description:str = obj["Description"]
      """  A decription for the UOMClass.  Mandatory.  """  
      self.ClassType:str = obj["ClassType"]
      """   defines the type of class. Valid values are; Length,Area,Weight,Volume,Count or Other  All except "Other" are considered standard types.  There can be only 1 uom class per standard class type.
Having a ClassType allows the system to filter the  list of uoms when only a certain type is the only logical choice. Such as the case when entering the length, width, height of a bin. In this case the only logical choice would be the UOMs that belong to the "Length" class.  """  
      self.BaseUOMCode:str = obj["BaseUOMCode"]
      """  Base Unit of Measure for the class. Mandatory to perfrom UOM conversions. Must be valid in UOMConv table of the UOMClass. The initial UOMConv record created will be set as the BaseUOM. The User will be able to change this if they need to once other UOMConv records are created.  BaseUOM  is the reference point for establishing conversion factors of the other uoms within the class (see UOMConv definitions). It always has a conversion factor of 1. Normally this is the smallest unit that you wish considered.  """  
      self.DefUomCode:str = obj["DefUomCode"]
      """   Indicates which UOM of the class should be used as the default when creating new parts using this class. Optional.
This replaces the 8.3 logic which used XASyst.DefaultUOM. (See also XASyst.DefUOMClassID)  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the UOMClass is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  """  
      self.GlobalUOMClass:bool = obj["GlobalUOMClass"]
      """  Marks this UOMClass as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultUOMClass:bool = obj["DefaultUOMClass"]
      """  Signifies this is the Default UOM Class.  This is stored in XASyst.DefUOMClassID.  Used as a default value when creating new Part masters.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UOMConvRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  The UOM Class ID that this unit of measure belongs to.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.ConvFactor:int = obj["ConvFactor"]
      """   Value used to convert to/from base uom. Expressed as 1 of the specific UOM in Base UOM if ConvOperator = *, else 1 Base UOM in UOM. For example: A Class of "Lengths" might have meter(m) as it's base . Kilometer(km) would have a  conversion factor of 1000(m) with ConvOperator = *. Mandatory if UOMClass.PartSpecific = false. If it's the BaseUOM must have conversion factor of 1. Simplified usage:To convert a quantity to base UOM you multiply by the ConvFactor.  Example, with meters as base. ft to meters 10ft * 0.3048 = 3.048m .. To convert base to uom of yard you divide the quantiy in base by the ConvFactor. Ex: 3.048 / 0.9144 = 3.33333yd.

Factors defined in UOMConv are not specific to any individual part and are considered standard  conversions. The relationship between Inches (in), and  Feet (ft) is a good example. 
Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table.  """  
      self.UOMDesc:str = obj["UOMDesc"]
      """  Long Description of a unit of measure. Mandatory.  """  
      self.BaseUOM83:bool = obj["BaseUOM83"]
      """  used only during the 8.3 to 9.0 conversion process.  """  
      self.UOMCode83:str = obj["UOMCode83"]
      """  Used only for the 8.3 to 9.0 conversion. Holds the original code that was used in 8.3. By changing the UOMCode the user can instruct the system to  convert the old 8.3 value to the new UOMCode value.  Example Ea to EACH or E to EACH.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the UOM is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  """  
      self.UOMSymbol:str = obj["UOMSymbol"]
      """  Optional Symbol that can be used in place of the UOMCode such as when printing external documents or certain displays. Especially useful to express a UOM using subscripts or superscripts which would be hard to use as a UOMCode due to difficultly of keying into transactions.  """  
      self.AllowDecimals:bool = obj["AllowDecimals"]
      """   Indicates if fractional quantities are allowed with this unit of measure.
If true, then NumOfDec and Rounding fields will be enabled and Precison must have a value greater than zero. 
Replaces the 8.03.400 Part.WholeUnit.  """  
      self.NumOfDec:int = obj["NumOfDec"]
      """   Defines how many decimal points are allowed with this UOM.
Disabled and set to zero if UOMConv.AllowDecimals = False. Enabled and must be > 0 if UOMConv.AllowDecimals = True. Not only does this validate quantity entered but also used in UOM quantity conversion logic.  """  
      self.Rounding:str = obj["Rounding"]
      """  If AllowDec = True,  then the following options are available; RND-  Round, Up-Round UP, DWN-Round Down.  """  
      self.StdUOM:bool = obj["StdUOM"]
      """  System set, indicates if this UOMConv exists in a Standard UOMClass. (UOMClass.ClassType <> "Other"). Used to provide list of UOMs when a UOMClass, or Target UOMCode is not known. Ex: Creating a JobMtl record against a non-part item. In this case all UOMConv where StdUOM = true are valid. It is also used during the UOMConv maint process.  Not allowed to create a UOMConv with with a UOMCode that exists in another standard UOMClass.  """  
      self.PartSpecific:bool = obj["PartSpecific"]
      """   Indicates if Part Specific Conversion factors are required. This can only set to true with ClassType = "Other". Setting this to true, disables entry of the UOM Conversion factors from within the UOM maint. In this case conversion factors of the uoms are relative to the Part and will be enter in Part maint.
Example: You stock in Sheets, Purchase in Lbs, and consume in Square Feet.  Since the number of Lbs and SqFt in a sheet are relative to a part they would be marked as PartSpecific = true.  """  
      self.HasBeenUsed:bool = obj["HasBeenUsed"]
      """  This indicates that this UOM Conv has been used somewhere.  Therefore we do not want to allow the associated conversion to change.  """  
      self.ConvOperator:str = obj["ConvOperator"]
      """   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  """  
      self.GlobalUOMConv:bool = obj["GlobalUOMConv"]
      """  Marks this UOMConv as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseUOM:bool = obj["BaseUOM"]
      """  Signifies this is the Base UOM for this Class  """  
      self.ConvFromUOM:str = obj["ConvFromUOM"]
      """  Qualifies that 1 of this uom = ConvFactor in ConvToUOM. Example: 12in = 1ft or 1ft = 12in  """  
      self.ConvToUOM:str = obj["ConvToUOM"]
      """  Qualifies UOM of the ConvFactor. This either the UOMClass.BaseUOM or the UOMConv.UOMCode depending on the value of ConvOperator.  """  
      self.DefaultUOM:bool = obj["DefaultUOM"]
      """  Sets a flag to determine whether this is the default UOM for this Class.  """  
      self.DispBaseUOMCode:str = obj["DispBaseUOMCode"]
      """  Display field for BaseUOMCode  """  
      self.EnableBaseUOM:bool = obj["EnableBaseUOM"]
      """  Flag which determines whether we should enable the BaseUOM field.  The rule is, if the current BaseUOM has the field HasBeenUsed = true, we shouldn't allow them to change the BaseUOM.  """  
      self.DispPkgCode:str = obj["DispPkgCode"]
      """  Used to input/display the package code related to the UOMClass/UOM (stored in table PackingUOM).  """  
      self.DispPkgCodeDesc:str = obj["DispPkgCodeDesc"]
      """  Description of the PkgCode  """  
      self.DispPkgDisplaySeq:int = obj["DispPkgDisplaySeq"]
      """  Indicates the display sequence of the packaging in relation to the other packaging for the UOMClass  """  
      self.DispPkgIsDefault:bool = obj["DispPkgIsDefault"]
      """  Indicates if the PkgCode is the default.  """  
      self.DispPkgDisplayHidden:bool = obj["DispPkgDisplayHidden"]
      """  Indicates if the package code will be displayed in the application.If false, the package codes that are not valid for the MFG process on the shop floor (MES) are hidden.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   uoMClassID
   """  
   def __init__(self, obj):
      self.uoMClassID:str = obj["uoMClassID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UOMClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  Unit of Measure Class Identifier.  User defined. Mandatory. Unique key component. Examples: Length, Volume, Weight,Roll,Bar,Sheet  """  
      self.Description:str = obj["Description"]
      """  A decription for the UOMClass.  Mandatory.  """  
      self.ClassType:str = obj["ClassType"]
      """   defines the type of class. Valid values are; Length,Area,Weight,Volume,Count or Other  All except "Other" are considered standard types.  There can be only 1 uom class per standard class type.
Having a ClassType allows the system to filter the  list of uoms when only a certain type is the only logical choice. Such as the case when entering the length, width, height of a bin. In this case the only logical choice would be the UOMs that belong to the "Length" class.  """  
      self.BaseUOMCode:str = obj["BaseUOMCode"]
      """  Base Unit of Measure for the class. Mandatory to perfrom UOM conversions. Must be valid in UOMConv table of the UOMClass. The initial UOMConv record created will be set as the BaseUOM. The User will be able to change this if they need to once other UOMConv records are created.  BaseUOM  is the reference point for establishing conversion factors of the other uoms within the class (see UOMConv definitions). It always has a conversion factor of 1. Normally this is the smallest unit that you wish considered.  """  
      self.DefUomCode:str = obj["DefUomCode"]
      """   Indicates which UOM of the class should be used as the default when creating new parts using this class. Optional.
This replaces the 8.3 logic which used XASyst.DefaultUOM. (See also XASyst.DefUOMClassID)  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the UOMClass is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  """  
      self.GlobalUOMClass:bool = obj["GlobalUOMClass"]
      """  Marks this UOMClass as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultUOMClass:bool = obj["DefaultUOMClass"]
      """  Signifies this is the Default UOM Class.  This is stored in XASyst.DefUOMClassID.  Used as a default value when creating new Part masters.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UOMClassListTableset:
   def __init__(self, obj):
      self.UOMClassList:list[Erp_Tablesets_UOMClassListRow] = obj["UOMClassList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UOMClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  Unit of Measure Class Identifier.  User defined. Mandatory. Unique key component. Examples: Length, Volume, Weight,Roll,Bar,Sheet  """  
      self.Description:str = obj["Description"]
      """  A decription for the UOMClass.  Mandatory.  """  
      self.ClassType:str = obj["ClassType"]
      """   defines the type of class. Valid values are; Length,Area,Weight,Volume,Count or Other  All except "Other" are considered standard types.  There can be only 1 uom class per standard class type.
Having a ClassType allows the system to filter the  list of uoms when only a certain type is the only logical choice. Such as the case when entering the length, width, height of a bin. In this case the only logical choice would be the UOMs that belong to the "Length" class.  """  
      self.BaseUOMCode:str = obj["BaseUOMCode"]
      """  Base Unit of Measure for the class. Mandatory to perfrom UOM conversions. Must be valid in UOMConv table of the UOMClass. The initial UOMConv record created will be set as the BaseUOM. The User will be able to change this if they need to once other UOMConv records are created.  BaseUOM  is the reference point for establishing conversion factors of the other uoms within the class (see UOMConv definitions). It always has a conversion factor of 1. Normally this is the smallest unit that you wish considered.  """  
      self.DefUomCode:str = obj["DefUomCode"]
      """   Indicates which UOM of the class should be used as the default when creating new parts using this class. Optional.
This replaces the 8.3 logic which used XASyst.DefaultUOM. (See also XASyst.DefUOMClassID)  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the UOMClass is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  """  
      self.GlobalUOMClass:bool = obj["GlobalUOMClass"]
      """  Marks this UOMClass as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultUOMClass:bool = obj["DefaultUOMClass"]
      """  Signifies this is the Default UOM Class.  This is stored in XASyst.DefUOMClassID.  Used as a default value when creating new Part masters.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UOMClassTableset:
   def __init__(self, obj):
      self.UOMClass:list[Erp_Tablesets_UOMClassRow] = obj["UOMClass"]
      self.UOMConv:list[Erp_Tablesets_UOMConvRow] = obj["UOMConv"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UOMConvRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """  The UOM Class ID that this unit of measure belongs to.  """  
      self.UOMCode:str = obj["UOMCode"]
      """  User defined code which uniquely identifies the UOM within the UOMClass.  """  
      self.ConvFactor:int = obj["ConvFactor"]
      """   Value used to convert to/from base uom. Expressed as 1 of the specific UOM in Base UOM if ConvOperator = *, else 1 Base UOM in UOM. For example: A Class of "Lengths" might have meter(m) as it's base . Kilometer(km) would have a  conversion factor of 1000(m) with ConvOperator = *. Mandatory if UOMClass.PartSpecific = false. If it's the BaseUOM must have conversion factor of 1. Simplified usage:To convert a quantity to base UOM you multiply by the ConvFactor.  Example, with meters as base. ft to meters 10ft * 0.3048 = 3.048m .. To convert base to uom of yard you divide the quantiy in base by the ConvFactor. Ex: 3.048 / 0.9144 = 3.33333yd.

Factors defined in UOMConv are not specific to any individual part and are considered standard  conversions. The relationship between Inches (in), and  Feet (ft) is a good example. 
Sometimes a unit of measure conversion is relative to a specific part. These are non-standard conversions.
For example; 1 box(bx) of  Part A is 12ea. 1(bx) of Part B is 24ea. Non-standard conversions are defined in the PartUOM table.  """  
      self.UOMDesc:str = obj["UOMDesc"]
      """  Long Description of a unit of measure. Mandatory.  """  
      self.BaseUOM83:bool = obj["BaseUOM83"]
      """  used only during the 8.3 to 9.0 conversion process.  """  
      self.UOMCode83:str = obj["UOMCode83"]
      """  Used only for the 8.3 to 9.0 conversion. Holds the original code that was used in 8.3. By changing the UOMCode the user can instruct the system to  convert the old 8.3 value to the new UOMCode value.  Example Ea to EACH or E to EACH.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the UOM is Active. If not Active system will no longer allow it to be used.  Does NOTvalidate if it has already been used.  """  
      self.UOMSymbol:str = obj["UOMSymbol"]
      """  Optional Symbol that can be used in place of the UOMCode such as when printing external documents or certain displays. Especially useful to express a UOM using subscripts or superscripts which would be hard to use as a UOMCode due to difficultly of keying into transactions.  """  
      self.AllowDecimals:bool = obj["AllowDecimals"]
      """   Indicates if fractional quantities are allowed with this unit of measure.
If true, then NumOfDec and Rounding fields will be enabled and Precison must have a value greater than zero. 
Replaces the 8.03.400 Part.WholeUnit.  """  
      self.NumOfDec:int = obj["NumOfDec"]
      """   Defines how many decimal points are allowed with this UOM.
Disabled and set to zero if UOMConv.AllowDecimals = False. Enabled and must be > 0 if UOMConv.AllowDecimals = True. Not only does this validate quantity entered but also used in UOM quantity conversion logic.  """  
      self.Rounding:str = obj["Rounding"]
      """  If AllowDec = True,  then the following options are available; RND-  Round, Up-Round UP, DWN-Round Down.  """  
      self.StdUOM:bool = obj["StdUOM"]
      """  System set, indicates if this UOMConv exists in a Standard UOMClass. (UOMClass.ClassType <> "Other"). Used to provide list of UOMs when a UOMClass, or Target UOMCode is not known. Ex: Creating a JobMtl record against a non-part item. In this case all UOMConv where StdUOM = true are valid. It is also used during the UOMConv maint process.  Not allowed to create a UOMConv with with a UOMCode that exists in another standard UOMClass.  """  
      self.PartSpecific:bool = obj["PartSpecific"]
      """   Indicates if Part Specific Conversion factors are required. This can only set to true with ClassType = "Other". Setting this to true, disables entry of the UOM Conversion factors from within the UOM maint. In this case conversion factors of the uoms are relative to the Part and will be enter in Part maint.
Example: You stock in Sheets, Purchase in Lbs, and consume in Square Feet.  Since the number of Lbs and SqFt in a sheet are relative to a part they would be marked as PartSpecific = true.  """  
      self.HasBeenUsed:bool = obj["HasBeenUsed"]
      """  This indicates that this UOM Conv has been used somewhere.  Therefore we do not want to allow the associated conversion to change.  """  
      self.ConvOperator:str = obj["ConvOperator"]
      """   Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).
For example for Feet to Inch where Inch is the base uom. 
You could have 1ft / 12 = 1In  """  
      self.GlobalUOMConv:bool = obj["GlobalUOMConv"]
      """  Marks this UOMConv as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseUOM:bool = obj["BaseUOM"]
      """  Signifies this is the Base UOM for this Class  """  
      self.ConvFromUOM:str = obj["ConvFromUOM"]
      """  Qualifies that 1 of this uom = ConvFactor in ConvToUOM. Example: 12in = 1ft or 1ft = 12in  """  
      self.ConvToUOM:str = obj["ConvToUOM"]
      """  Qualifies UOM of the ConvFactor. This either the UOMClass.BaseUOM or the UOMConv.UOMCode depending on the value of ConvOperator.  """  
      self.DefaultUOM:bool = obj["DefaultUOM"]
      """  Sets a flag to determine whether this is the default UOM for this Class.  """  
      self.DispBaseUOMCode:str = obj["DispBaseUOMCode"]
      """  Display field for BaseUOMCode  """  
      self.EnableBaseUOM:bool = obj["EnableBaseUOM"]
      """  Flag which determines whether we should enable the BaseUOM field.  The rule is, if the current BaseUOM has the field HasBeenUsed = true, we shouldn't allow them to change the BaseUOM.  """  
      self.DispPkgCode:str = obj["DispPkgCode"]
      """  Used to input/display the package code related to the UOMClass/UOM (stored in table PackingUOM).  """  
      self.DispPkgCodeDesc:str = obj["DispPkgCodeDesc"]
      """  Description of the PkgCode  """  
      self.DispPkgDisplaySeq:int = obj["DispPkgDisplaySeq"]
      """  Indicates the display sequence of the packaging in relation to the other packaging for the UOMClass  """  
      self.DispPkgIsDefault:bool = obj["DispPkgIsDefault"]
      """  Indicates if the PkgCode is the default.  """  
      self.DispPkgDisplayHidden:bool = obj["DispPkgDisplayHidden"]
      """  Indicates if the package code will be displayed in the application.If false, the package codes that are not valid for the MFG process on the shop floor (MES) are hidden.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtUOMClassTableset:
   def __init__(self, obj):
      self.UOMClass:list[Erp_Tablesets_UOMClassRow] = obj["UOMClass"]
      self.UOMConv:list[Erp_Tablesets_UOMConvRow] = obj["UOMConv"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   uoMClassID
   """  
   def __init__(self, obj):
      self.uoMClassID:str = obj["uoMClassID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_UOMClassTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_UOMClassTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_UOMClassTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_UOMClassListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewUOMClass_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

class GetNewUOMClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUOMConv_input:
   """ Required : 
   ds
   uoMClassID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      self.uoMClassID:str = obj["uoMClassID"]
      pass

class GetNewUOMConv_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseUOMClass
   whereClauseUOMConv
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseUOMClass:str = obj["whereClauseUOMClass"]
      self.whereClauseUOMConv:str = obj["whereClauseUOMConv"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_UOMClassTableset] = obj["returnObj"]
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

class OnChangeAllowDecimal_input:
   """ Required : 
   uomClassID
   uomCode
   newAllowDec
   ds
   """  
   def __init__(self, obj):
      self.uomClassID:str = obj["uomClassID"]
      """  UOMClassID  """  
      self.uomCode:str = obj["uomCode"]
      """  UOMCode  """  
      self.newAllowDec:bool = obj["newAllowDec"]
      """  Proposed value for AllowDec  """  
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

class OnChangeAllowDecimal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBaseUOM_input:
   """ Required : 
   uomClassID
   uomCode
   newBaseUOM
   ds
   """  
   def __init__(self, obj):
      self.uomClassID:str = obj["uomClassID"]
      """  UOMClassID.  """  
      self.uomCode:str = obj["uomCode"]
      """  Old UOMCode  """  
      self.newBaseUOM:bool = obj["newBaseUOM"]
      """  Proposed BaseUOMCode  """  
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

class OnChangeBaseUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeClassType_input:
   """ Required : 
   uomClassID
   newClassType
   ds
   """  
   def __init__(self, obj):
      self.uomClassID:str = obj["uomClassID"]
      """  UOMClassID.  """  
      self.newClassType:str = obj["newClassType"]
      """  Proposed ClassType.  """  
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

class OnChangeClassType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDispPkgDisplaySeq_input:
   """ Required : 
   uomClassID
   uomCode
   newDispPkgDisplaySeq
   ds
   """  
   def __init__(self, obj):
      self.uomClassID:str = obj["uomClassID"]
      """  UOMClassID.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOMCode  """  
      self.newDispPkgDisplaySeq:int = obj["newDispPkgDisplaySeq"]
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

class OnChangeDispPkgDisplaySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePkgCode_input:
   """ Required : 
   uomClassID
   uomCode
   pkgCode
   ds
   """  
   def __init__(self, obj):
      self.uomClassID:str = obj["uomClassID"]
      """  UOMClassID.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOMCode  """  
      self.pkgCode:str = obj["pkgCode"]
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

class OnChangePkgCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUOMCode_input:
   """ Required : 
   uomCode
   ds
   """  
   def __init__(self, obj):
      self.uomCode:str = obj["uomCode"]
      """  Proposed UOMCode.  """  
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

class OnChangeUOMCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtUOMClassTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtUOMClassTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UOMClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateUOMClassId_input:
   """ Required : 
   ipUOMClassID
   OP_Result
   """  
   def __init__(self, obj):
      self.ipUOMClassID:str = obj["ipUOMClassID"]
      self.OP_Result:bool = obj["OP_Result"]
      pass

class ValidateUOMClassId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.OP_Result:bool = obj["OP_Result"]
      pass

      """  output parameters  """  

