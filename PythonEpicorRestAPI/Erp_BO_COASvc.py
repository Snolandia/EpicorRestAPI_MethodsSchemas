import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.COASvc
# Description: Chart of Accounts structure maintenance application
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_COAs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COAs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs",headers=creds) as resp:
           return await resp.json()

async def post_COAs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COAs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COAs_Company_COACode(Company, COACode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COA item
   Description: Calls GetByID to retrieve the COA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COAs_Company_COACode(Company, COACode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COA for the service
   Description: Calls UpdateExt to update COA. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COAs_Company_COACode(Company, COACode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COA item
   Description: Call UpdateExt to delete COA item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COA
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")",headers=creds) as resp:
           return await resp.json()

async def get_COAs_Company_COACode_COASegments(Company, COACode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get COASegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")/COASegments",headers=creds) as resp:
           return await resp.json()

async def get_COAs_Company_COACode_COASegments_Company_COACode_SegmentNbr(Company, COACode, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegment item
   Description: Calls GetByID to retrieve the COASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COAs(" + Company + "," + COACode + ")/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COASegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments",headers=creds) as resp:
           return await resp.json()

async def post_COASegments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COASegments_Company_COACode_SegmentNbr(Company, COACode, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegment item
   Description: Calls GetByID to retrieve the COASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COASegments_Company_COACode_SegmentNbr(Company, COACode, SegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COASegment for the service
   Description: Calls UpdateExt to update COASegment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COASegments_Company_COACode_SegmentNbr(Company, COACode, SegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COASegment item
   Description: Call UpdateExt to delete COASegment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegmentNotCreateds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COASegmentNotCreateds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegmentNotCreateds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegmentNotCreatedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds",headers=creds) as resp:
           return await resp.json()

async def post_COASegmentNotCreateds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegmentNotCreateds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegmentNotCreatedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegmentNotCreatedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COASegmentNotCreateds_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegmentNotCreated item
   Description: Calls GetByID to retrieve the COASegmentNotCreated item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegmentNotCreated
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegmentNotCreatedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COASegmentNotCreateds_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COASegmentNotCreated for the service
   Description: Calls UpdateExt to update COASegmentNotCreated. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegmentNotCreated
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegmentNotCreatedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COASegmentNotCreateds_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COASegmentNotCreated item
   Description: Call UpdateExt to delete COASegmentNotCreated item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegmentNotCreated
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/COASegmentNotCreateds(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCOA, whereClauseCOASegment, whereClauseCOASegmentNotCreated, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseCOA=" + whereClauseCOA
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCOASegment=" + whereClauseCOASegment
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCOASegmentNotCreated=" + whereClauseCOASegmentNotCreated
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(coACode, epicorHeaders = None):
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
   params += "coACode=" + coACode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCOAGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCOAGlobalFields
   OperationID: GetCOAGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOAGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOAGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCOASegmentGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCOASegmentGlobalFields
   OperationID: GetCOASegmentGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOASegmentGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOASegmentGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildCOASegmentList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildCOASegmentList
   Description: Build list of segment numbers/names
   OperationID: BuildCOASegmentList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCOASegmentList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCOASegmentList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDOrdered(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDOrdered
   Description: Returns COATableset object by requested COACode for Kinetic
   OperationID: GetByIDOrdered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDOrdered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDOrdered_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCOAGlobalCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCOAGlobalCOA
   Description: Method to call when changing the global COA flag on a COA.
Assigns the GlbFlag base on the new value.
   OperationID: ChangeCOAGlobalCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCOAGlobalCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCOAGlobalCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCOASegmentGlobalCOASegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCOASegmentGlobalCOASegment
   Description: Method to call when changing the global COA Segment flag on a COASegment.
Assigns the GlbFlag base on the new value.
   OperationID: ChangeCOASegmentGlobalCOASegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCOASegmentGlobalCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCOASegmentGlobalCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGlobalValuesLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGlobalValuesLock
   Description: Method call when changing the Global Values Lock flag on a segment.
   OperationID: ChangeGlobalValuesLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGlobalValuesLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlobalValuesLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSiteSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSiteSegment
   Description: This method should be called when COASegment SiteSegment changes
   OperationID: ChangeSiteSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSiteSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSiteSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsSegValInUse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsSegValInUse
   Description: Determine if a specific segment value has been used in either a GLAccount
or on a GLJrnDtl.
   OperationID: IsSegValInUse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsSegValInUse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsSegValInUse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAllowAlpha(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAllowAlpha
   Description: Check to see if the segment can have the alpha seg values set to no.
   OperationID: CheckAllowAlpha
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAllowAlpha_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAllowAlpha_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCOALengthWithSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCOALengthWithSegment
   Description: Calculate the total length of the COA (sum of the COASegment.Maxlength)
   OperationID: CheckCOALengthWithSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOALengthWithSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOALengthWithSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckChartLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckChartLength
   Description: Calculate the total length of the COA (sum of the COASegment.Maxlength)
   OperationID: CheckChartLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChartLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChartLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckConsolidatedCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckConsolidatedCOA
   Description: Determine if the COA has a consolidation definition
   OperationID: CheckConsolidatedCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConsolidatedCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConsolidatedCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsCOAMasterCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsCOAMasterCOA
   Description: Determine if the COA is the Master COA
   OperationID: IsCOAMasterCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsCOAMasterCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsCOAMasterCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsChartUsedInTransaction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsChartUsedInTransaction
   Description: Determine if the Chart has be used by a transaction
   OperationID: IsChartUsedInTransaction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsChartUsedInTransaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsChartUsedInTransaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsChartInUse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsChartInUse
   Description: Checks if COA is assigned to a GLBook or a GLAccount record exists for the COA.
   OperationID: IsChartInUse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsChartInUse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsChartInUse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBalanceChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBalanceChange
   Description: Determines if a balance segment is changing, and if it is, checks
if a budget is setup.  If it is, and the number of balance segments are
being increased, informs the user the budgets may be invalid with this change.
   OperationID: CheckBalanceChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBalanceChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBalanceChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDynamic(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDynamic
   Description: Ensure the natural account is not flagged as a dynamic segment
   OperationID: CheckDynamic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDynamic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDynamic_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIfDeletingLastSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIfDeletingLastSegment
   Description: Used to determine if the user is deleting the last defined segment or a previous one.
If the segment is not the last defined, then the delete process must resequence all existing
segment records and their associated records including the segment values.
The overhead that may be associated with this operation has the potential to be huge
so we will make sure this is what the user really wants.
   OperationID: CheckIfDeletingLastSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfDeletingLastSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfDeletingLastSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIfSegmentHasValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIfSegmentHasValues
   Description: Used to determine if the user is deleting the segment having values.
   OperationID: CheckIfSegmentHasValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIfSegmentHasValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIfSegmentHasValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRebuildBalances(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRebuildBalances
   OperationID: CheckRebuildBalances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRebuildBalances_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRebuildBalances_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSeparatorChar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSeparatorChar
   Description: Validate the separator character
   OperationID: CheckSeparatorChar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSeparatorChar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSeparatorChar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckUseRefEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckUseRefEntity
   Description: Validates COASegment reference entity related fields
   OperationID: CheckUseRefEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckUseRefEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckUseRefEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_COAStructureChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method COAStructureChange
   Description: Resync the temp table due to a COA structure change
   OperationID: COAStructureChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/COAStructureChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/COAStructureChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_COAExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method COAExists
   OperationID: COAExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/COAExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/COAExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteAndRenumberSegments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteAndRenumberSegments
   Description: Deletes requested segment number and renumbers the remaining.  For example,
chart has 3 segments and segment 2 is deleted.  This method renumbers segment3 as
segment 2.  The segment write trigger updates subordinate tables.
   OperationID: DeleteAndRenumberSegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAndRenumberSegments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAndRenumberSegments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveOnePosition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveOnePosition
   Description: This method moves the COASegment Display Order Up/Down one position in the
grid and returns the whole updated datatable.
   OperationID: MoveOnePosition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveOnePosition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveOnePosition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PromptAutoCreateDynSegVals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PromptAutoCreateDynSegVals
   Description: Ask the user if the COASegValues entries are to be created when the
COASegment record is saved.
   OperationID: PromptAutoCreateDynSegVals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PromptAutoCreateDynSegVals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromptAutoCreateDynSegVals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetRefEntityFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetRefEntityFields
   Description: Set COASegment Reference Entity related fields based upon the value of COASegment.RefEntity
   OperationID: SetRefEntityFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetRefEntityFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetRefEntityFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCOADynamicSegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCOADynamicSegValues
   Description: Update the COASegValues for the requested dynamic segment
   OperationID: UpdateCOADynamicSegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCOADynamicSegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCOADynamicSegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDynamicSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDynamicSegment
   Description: Updates the fields associated with the Dynamic setting.
   OperationID: UpdateDynamicSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDynamicSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDynamicSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateNatural(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateNatural
   Description: Updates the fields associated with the Global COA setting.
   OperationID: UpdateNatural
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateNatural_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNatural_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateFieldLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateFieldLength
   Description: Updates SegValueFieldLength based on new SegValueField value.
   OperationID: UpdateFieldLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateFieldLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateFieldLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEntryControl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEntryControl
   Description: Validate entry control
   OperationID: ValidateEntryControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEntryControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEntryControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRefEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRefEntity
   Description: Validate the reference entity against the BusEntity table.  If it
is valid send back a message asking users if they want the COASegValues
automatically created.
   OperationID: ValidateRefEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRefEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRefEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSegmentMaxLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSegmentMaxLength
   Description: Enforce maximum length rules for a segment
   OperationID: ValidateSegmentMaxLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSegmentMaxLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSegmentMaxLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSegmentMinLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSegmentMinLength
   Description: Enforce minimum length rules for a segment
   OperationID: ValidateSegmentMinLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSegmentMinLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSegmentMinLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WarnNewMandatorySegmentDynamic(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WarnNewMandatorySegmentDynamic
   Description: Check whether new segment is mandatory before adding it into existing COA.
   OperationID: WarnNewMandatorySegmentDynamic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNewMandatorySegmentDynamic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNewMandatorySegmentDynamic_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WarnNewMandatorySegmentDynamicExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WarnNewMandatorySegmentDynamicExt
   Description: Check whether segment is new and mandatory before import it into existing COA.
   OperationID: WarnNewMandatorySegmentDynamicExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNewMandatorySegmentDynamicExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNewMandatorySegmentDynamicExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckGlobalCOASegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckGlobalCOASegment
   OperationID: CheckGlobalCOASegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGlobalCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGlobalCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMaxLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMaxLength
   Description: Calc Chart length field
   OperationID: UpdateMaxLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMaxLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaxLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMaxLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMaxLength
   Description: Calc Chart length field
   OperationID: GetMaxLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMaxLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMaxLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveOnePositionReturnNewIndex(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveOnePositionReturnNewIndex
   Description: This method moves the COASegment Display Order Up/Down one position in the
grid and returns the whole updated datatable for Kinetic
   OperationID: MoveOnePositionReturnNewIndex
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveOnePositionReturnNewIndex_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveOnePositionReturnNewIndex_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOA
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOASegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOASegment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COASvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COAListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COARow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentNotCreatedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COASegmentNotCreatedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegmentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COASegmentRow] = obj["value"]
      pass

class Erp_Tablesets_COAListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Marks the COA as Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if the chart has been used  """  
      self.ChartLength:int = obj["ChartLength"]
      """  Sum of the COASegment.MaxLength entries.  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.NbrSegments:int = obj["NbrSegments"]
      """  Total number of segments defined for this COA  """  
      self.HasRefSegment:bool = obj["HasRefSegment"]
      """  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  """  
      self.ConsInUse:bool = obj["ConsInUse"]
      """  Logical indicating if this chart of accounts is subject to consolidation  """  
      self.RebuildBalances:bool = obj["RebuildBalances"]
      """  Logical indicating the balances are to be rebuilt due to a change in balance structure  """  
      self.CreateDefCat:bool = obj["CreateDefCat"]
      """  Logical indicating if default categories are to be created  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Marks the COA as Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.PESunatCOA:str = obj["PESunatCOA"]
      """  Peru CSF: SUNAT Chart of Accounts Code  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if the chart has been used  """  
      self.CreateDefCat:bool = obj["CreateDefCat"]
      """  Logical indicating if default categories are to be created  """  
      self.EnableGlobalCOA:bool = obj["EnableGlobalCOA"]
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.HasRefSegment:bool = obj["HasRefSegment"]
      """  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.NbrSegments:int = obj["NbrSegments"]
      """  Total number of segments defined for this COA  """  
      self.RebuildBalances:bool = obj["RebuildBalances"]
      """  Logical indicating the balances are to be rebuilt due to a change in balance structure  """  
      self.ChartLength:int = obj["ChartLength"]
      """  Sum of the COASegment.MaxLength entries.  """  
      self.ConsInUse:bool = obj["ConsInUse"]
      """  Logical indicating if this chart of accounts is subject to consolidation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegmentNotCreatedRow:
   def __init__(self, obj):
      self.SegmentCode:str = obj["SegmentCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.MaxLength:int = obj["MaxLength"]
      """  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  """  
      self.MinLength:int = obj["MinLength"]
      """  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  """  
      self.Dynamic:bool = obj["Dynamic"]
      """  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  """  
      self.UseRefEntity:bool = obj["UseRefEntity"]
      """  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  """  
      self.AllowAlpha:bool = obj["AllowAlpha"]
      """  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  """  
      self.EntryControl:str = obj["EntryControl"]
      """   Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegOpt table.
2 (two) - GL Reference Account Mask - only valid for segments defined as Use Ref Entity where the reference entity = 'Reference Entity'.
3 (three) - Optional.  The segment is not required to be entered.  """  
      self.SegSelfBal:bool = obj["SegSelfBal"]
      """  Indicates if journal entries are automatically balanced.  """  
      self.Level:int = obj["Level"]
      """  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  """  
      self.SummaryBal:bool = obj["SummaryBal"]
      """  Indicates if this segment is included in the summary balance GL Account.  Only those segments that are flagged as detail balance segments are eligible to be included as a summary balance segment.  """  
      self.DetailBal:bool = obj["DetailBal"]
      """  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  """  
      self.KeepOpenBal:bool = obj["KeepOpenBal"]
      """  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for project accounting where you want to keep the project date balance independent of the financial year.  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  """  
      self.AutoCreateSegVals:bool = obj["AutoCreateSegVals"]
      """  Indicates if segment values for segments defined as reference entity are to be created each time a new record is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  """  
      self.SelfBalAcct:str = obj["SelfBalAcct"]
      """  Account used  when creating balancing transactions for this segment.  """  
      self.BalSegValue1:str = obj["BalSegValue1"]
      """  Balance Seg Value 1  """  
      self.BalSegValue2:str = obj["BalSegValue2"]
      """  Balance Seg Value 2  """  
      self.BalSegValue3:str = obj["BalSegValue3"]
      """  Balance Seg Value 3  """  
      self.BalSegValue4:str = obj["BalSegValue4"]
      """  Balance Seg Value 4  """  
      self.BalSegValue5:str = obj["BalSegValue5"]
      """  Balance Seg Value 5  """  
      self.BalSegValue6:str = obj["BalSegValue6"]
      """  Balance Seg Value 6  """  
      self.BalSegValue7:str = obj["BalSegValue7"]
      """  Balance Seg Value 7  """  
      self.BalSegValue8:str = obj["BalSegValue8"]
      """  Balance Seg Value 8  """  
      self.BalSegValue9:str = obj["BalSegValue9"]
      """  Balance Seg Value 9  """  
      self.BalSegValue10:str = obj["BalSegValue10"]
      """  Balance Seg Value 10  """  
      self.BalSegValue11:str = obj["BalSegValue11"]
      """  Balance Seg Value 11  """  
      self.BalSegValue12:str = obj["BalSegValue12"]
      """  Balance Seg Value 12  """  
      self.BalSegValue13:str = obj["BalSegValue13"]
      """  Balance Seg Value 13  """  
      self.BalSegValue14:str = obj["BalSegValue14"]
      """  Balance Seg Value 14  """  
      self.BalSegValue15:str = obj["BalSegValue15"]
      """  Balance Seg Value 15  """  
      self.BalSegValue16:str = obj["BalSegValue16"]
      """  Balance Seg Value 16  """  
      self.BalSegValue17:str = obj["BalSegValue17"]
      """  Balance Seg Value 17  """  
      self.BalSegValue18:str = obj["BalSegValue18"]
      """  Balance Seg Value 18  """  
      self.BalSegValue19:str = obj["BalSegValue19"]
      """  Balance Seg Value 19  """  
      self.BalSegValue20:str = obj["BalSegValue20"]
      """  Balance Seg Value 20  """  
      self.SelfOffAcct:str = obj["SelfOffAcct"]
      """  The Self Balance offset account used when balancing this segment.  """  
      self.OffSegValue1:str = obj["OffSegValue1"]
      """  Offset Segment Value 1  """  
      self.OffSegValue2:str = obj["OffSegValue2"]
      """  Offset Segment Value 2  """  
      self.OffSegValue3:str = obj["OffSegValue3"]
      """  Offset Segment Value 3  """  
      self.OffSegValue4:str = obj["OffSegValue4"]
      """  Offset Segment Value 4  """  
      self.OffSegValue5:str = obj["OffSegValue5"]
      """  Offset Segment Value 5  """  
      self.OffSegValue6:str = obj["OffSegValue6"]
      """  Offset Segment Value 6  """  
      self.OffSegValue7:str = obj["OffSegValue7"]
      """  Offset Segment Value 7  """  
      self.OffSegValue8:str = obj["OffSegValue8"]
      """  Offset Segment Value 8  """  
      self.OffSegValue9:str = obj["OffSegValue9"]
      """  Offset Segment Value 9  """  
      self.OffSegValue10:str = obj["OffSegValue10"]
      """  Offset Segment Value 10  """  
      self.OffSegValue11:str = obj["OffSegValue11"]
      """  Offset Segment Value 11  """  
      self.OffSegValue12:str = obj["OffSegValue12"]
      """  Offset Segment Value 12  """  
      self.OffSegValue13:str = obj["OffSegValue13"]
      """  Offset Segment Value 13  """  
      self.OffSegValue14:str = obj["OffSegValue14"]
      """  Offset Segment Value 14  """  
      self.OffSegValue15:str = obj["OffSegValue15"]
      """  Offset Segment Value 15  """  
      self.OffSegValue16:str = obj["OffSegValue16"]
      """  Offset Segment Value 16  """  
      self.OffSegValue17:str = obj["OffSegValue17"]
      """  Offset Segment Value 17  """  
      self.OffSegValue18:str = obj["OffSegValue18"]
      """  Offset Segment Value 18  """  
      self.OffSegValue19:str = obj["OffSegValue19"]
      """  Offset Segment Value 19  """  
      self.OffSegValue20:str = obj["OffSegValue20"]
      """  Offset Segment Value 20  """  
      self.ReverseCategoryID:str = obj["ReverseCategoryID"]
      """  Reverse Account Category.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNIsCFICode:bool = obj["CNIsCFICode"]
      """  CNIsCFICode  """  
      self.SegValueField:str = obj["SegValueField"]
      """  The name of Business Entity field that represents segment value.  """  
      self.DescFieldName:str = obj["DescFieldName"]
      """  The name of Business Entity field that represents description of segment value.  """  
      self.GlobalCOASegment:bool = obj["GlobalCOASegment"]
      """  Marks the COASegment as Global  """  
      self.GlobalCOASegmentValues:bool = obj["GlobalCOASegmentValues"]
      """  Indicates COASegValues records for the COASegment will be used for Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.GlobalValuesLock:bool = obj["GlobalValuesLock"]
      """  Disables Segment Values record from receiving global updates  """  
      self.SiteSegment:bool = obj["SiteSegment"]
      """  Indicates this is a Site Segment  """  
      self.BalancingAcctDesc:str = obj["BalancingAcctDesc"]
      """  Balancing Account Description  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if a chart is in use  """  
      self.DisplayedLast:bool = obj["DisplayedLast"]
      """  Internal field not meant for end user use.  Logical used by row rules to disable the move up/down buttons on the display order tab.  """  
      self.OffsetAcctDesc:str = obj["OffsetAcctDesc"]
      """  Offset Account Description  """  
      self.SegmentInUse:bool = obj["SegmentInUse"]
      """  Logical indicates if a COAsegment has been used in a GL Account.  """  
      self.StructureFmtChg:bool = obj["StructureFmtChg"]
      """  Internal field not meant for end user use.  Logical indicating if a critical COA structure change has occurred.  """  
      self.UpdatedAuto:bool = obj["UpdatedAuto"]
      """  Dynamic Segment values using Business Entity will 'Updated Automatically'. Business Entity (DB table) should have additional code triggers. (e.g. Customer, Vendor)  """  
      self.AutoCreateSegValsInfo:str = obj["AutoCreateSegValsInfo"]
      self.EnableGlobalSeg:bool = obj["EnableGlobalSeg"]
      self.EnableGlobalSegLock:bool = obj["EnableGlobalSegLock"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.EnableGlobalSegValues:bool = obj["EnableGlobalSegValues"]
      self.EnableGlobalSegValuesLock:bool = obj["EnableGlobalSegValuesLock"]
      self.GlbValuesFlag:bool = obj["GlbValuesFlag"]
      self.SegValueFieldLength:int = obj["SegValueFieldLength"]
      """  Length of Business Entity field that represents segment value.  """  
      self.SiteIsLegalEntity:bool = obj["SiteIsLegalEntity"]
      """  Site is a Legal Entity  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BusEntityDescDescription:str = obj["BusEntityDescDescription"]
      self.BusEntityDescEntityType:str = obj["BusEntityDescEntityType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildCOASegmentList_input:
   """ Required : 
   coaCode
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA Code  """  
      pass

class BuildCOASegmentList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of segments  """  
      pass

class COAExists_input:
   """ Required : 
   ipCOACode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      pass

class COAExists_output:
   def __init__(self, obj):
      pass

class COAStructureChange_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class COAStructureChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCOAGlobalCOA_input:
   """ Required : 
   ProposedGlobalCOA
   ds
   """  
   def __init__(self, obj):
      self.ProposedGlobalCOA:bool = obj["ProposedGlobalCOA"]
      """  The proposed global COA value  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class ChangeCOAGlobalCOA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCOASegmentGlobalCOASegment_input:
   """ Required : 
   flagtype
   ProposedGlobalFlag
   ds
   """  
   def __init__(self, obj):
      self.flagtype:str = obj["flagtype"]
      """  Use 'Segment' to change GlobalCOASegment or any other to change GlobalCOASegmentValues  """  
      self.ProposedGlobalFlag:bool = obj["ProposedGlobalFlag"]
      """  The proposed flag value  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class ChangeCOASegmentGlobalCOASegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGlobalValuesLock_input:
   """ Required : 
   ProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ProposedValue:bool = obj["ProposedValue"]
      """  The proposed Global Values Lock value  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class ChangeGlobalValuesLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSiteSegment_input:
   """ Required : 
   siteSegment
   checkForResponse
   ds
   """  
   def __init__(self, obj):
      self.siteSegment:bool = obj["siteSegment"]
      self.checkForResponse:bool = obj["checkForResponse"]
      """  Continue process based on user response  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class ChangeSiteSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.responseMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckAllowAlpha_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   ipProposedAlpha
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  Chart of Account  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  SegmentNumber  """  
      self.ipProposedAlpha:bool = obj["ipProposedAlpha"]
      """  proposed alpha seg value  """  
      pass

class CheckAllowAlpha_output:
   def __init__(self, obj):
      pass

class CheckBalanceChange_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class CheckBalanceChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      self.ipMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckCOALengthWithSegment_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   ipProposedlength
   ipInAddMode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  Chart of Account  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  SegmentNumber  """  
      self.ipProposedlength:int = obj["ipProposedlength"]
      """  segment maximum length  """  
      self.ipInAddMode:bool = obj["ipInAddMode"]
      """  indicates if segment is being added  """  
      pass

class CheckCOALengthWithSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opChartLength:int = obj["parameters"]
      pass

      """  output parameters  """  

class CheckChartLength_input:
   """ Required : 
   ipCOACode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  Chart of Account  """  
      pass

class CheckChartLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opChartLength:int = obj["parameters"]
      pass

      """  output parameters  """  

class CheckConsolidatedCOA_input:
   """ Required : 
   ipCOACode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  Chart of Account  """  
      pass

class CheckConsolidatedCOA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opConsInUse:bool = obj["opConsInUse"]
      pass

      """  output parameters  """  

class CheckDynamic_input:
   """ Required : 
   ipDynamic
   ds
   """  
   def __init__(self, obj):
      self.ipDynamic:bool = obj["ipDynamic"]
      """  Proposed value of COASegment.Dynamic  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class CheckDynamic_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckGlobalCOASegment_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   ipGlobalCOASegmentFlag
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      self.ipGlobalCOASegmentFlag:bool = obj["ipGlobalCOASegmentFlag"]
      pass

class CheckGlobalCOASegment_output:
   def __init__(self, obj):
      pass

class CheckIfDeletingLastSegment_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  Chart of Accounts Code  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment Number the user wants to delete  """  
      pass

class CheckIfDeletingLastSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarningMsg:str = obj["parameters"]
      self.opRenumberRequired:bool = obj["opRenumberRequired"]
      pass

      """  output parameters  """  

class CheckIfSegmentHasValues_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  Chart of Accounts Code  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment Number the user wants to delete  """  
      pass

class CheckIfSegmentHasValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckRebuildBalances_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class CheckRebuildBalances_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckSeparatorChar_input:
   """ Required : 
   ipSepChar
   ipCOACode
   """  
   def __init__(self, obj):
      self.ipSepChar:str = obj["ipSepChar"]
      """  proposed separator character  """  
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      pass

class CheckSeparatorChar_output:
   def __init__(self, obj):
      pass

class CheckUseRefEntity_input:
   """ Required : 
   ipUseRefEntity
   ds
   """  
   def __init__(self, obj):
      self.ipUseRefEntity:bool = obj["ipUseRefEntity"]
      """  Proposed value of COASegment.UseRefEntity  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class CheckUseRefEntity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteAndRenumberSegments_input:
   """ Required : 
   ipCOACode
   ipSegDelete
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipSegDelete:int = obj["ipSegDelete"]
      """  Segment Number to Delete  """  
      pass

class DeleteAndRenumberSegments_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COATableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   coACode
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_COAListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Marks the COA as Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if the chart has been used  """  
      self.ChartLength:int = obj["ChartLength"]
      """  Sum of the COASegment.MaxLength entries.  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.NbrSegments:int = obj["NbrSegments"]
      """  Total number of segments defined for this COA  """  
      self.HasRefSegment:bool = obj["HasRefSegment"]
      """  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  """  
      self.ConsInUse:bool = obj["ConsInUse"]
      """  Logical indicating if this chart of accounts is subject to consolidation  """  
      self.RebuildBalances:bool = obj["RebuildBalances"]
      """  Logical indicating the balances are to be rebuilt due to a change in balance structure  """  
      self.CreateDefCat:bool = obj["CreateDefCat"]
      """  Logical indicating if default categories are to be created  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COAListTableset:
   def __init__(self, obj):
      self.COAList:list[Erp_Tablesets_COAListRow] = obj["COAList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_COARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.Description:str = obj["Description"]
      """  The description or Name of this Chart of Accounts.  """  
      self.SeparatorChar:str = obj["SeparatorChar"]
      """  This is the character that is displayed between each segment of the GL Accounts.  Tilde (~~), Tick (`) and Vertical Bar (|) are invalid separators.  """  
      self.PerBalFmt:str = obj["PerBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the period balance account.  Example: 1~2~5 indicates segments 1, 2 and 5 are used to construct the balance account number.  """  
      self.TBBalFmt:str = obj["TBBalFmt"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the segments used in the trial balance account. Example: 1~3~4 indicates segments 1, 3 and 4 are used to construct the balance account number.  """  
      self.FmtChgDate:str = obj["FmtChgDate"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.FmtChgTime:int = obj["FmtChgTime"]
      """  Internal field used by the GL Account Control to identify when cache needs to be updated with the new COA structure.  This is updated by the COASegment write and delete triggers.  It is not intended for end user use.  Only changes important to the GL Account control updates this field's value.  """  
      self.CtrlSegList:str = obj["CtrlSegList"]
      """  Internally used field.  Not intended for end-user use.  Tilde delimited string indicating the controlled segments.  Example: 1~2~5 indicates segments 1, 2 and 5 are controlled.  This field is to be used in those situations where reading all of the COASegements via the Dynamic index is too much overhead.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOA:bool = obj["GlobalCOA"]
      """  Marks the COA as Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.PESunatCOA:str = obj["PESunatCOA"]
      """  Peru CSF: SUNAT Chart of Accounts Code  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if the chart has been used  """  
      self.CreateDefCat:bool = obj["CreateDefCat"]
      """  Logical indicating if default categories are to be created  """  
      self.EnableGlobalCOA:bool = obj["EnableGlobalCOA"]
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.HasRefSegment:bool = obj["HasRefSegment"]
      """  logical indicating if this chart has a segment defined as use ref entity where the reference entity = GLCOARefType  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.NbrSegments:int = obj["NbrSegments"]
      """  Total number of segments defined for this COA  """  
      self.RebuildBalances:bool = obj["RebuildBalances"]
      """  Logical indicating the balances are to be rebuilt due to a change in balance structure  """  
      self.ChartLength:int = obj["ChartLength"]
      """  Sum of the COASegment.MaxLength entries.  """  
      self.ConsInUse:bool = obj["ConsInUse"]
      """  Logical indicating if this chart of accounts is subject to consolidation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegmentNotCreatedRow:
   def __init__(self, obj):
      self.SegmentCode:str = obj["SegmentCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COASegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment  """  
      self.Abbreviation:str = obj["Abbreviation"]
      """  Short name of segment.  """  
      self.MaxLength:int = obj["MaxLength"]
      """  Maximum length of the code used for this segment.  Valid values are between 1 and 50.  This value must be at least the value of the minimum length.  The minimum length is the default value.  If a segment is tied to a reference entity the maximum length cannot be less then the length of the reference entity's field.  """  
      self.MinLength:int = obj["MinLength"]
      """  Minimum length of the code to be used for this segment.  Must be a value between 1 and the maximum length.  If the segment is tied to a reference entity the minimum length cannot be greater than the length of the reference entity field.  """  
      self.Dynamic:bool = obj["Dynamic"]
      """  Indicates if accounts with this segment can be created on the fly when posting transactions.  If Yes, the GLAccount table does not have to contain entries with this field populated.  If No, then all valid combinations of segment values (COASegVal) must be defined in the GLAccount table before the account can be used.  """  
      self.UseRefEntity:bool = obj["UseRefEntity"]
      """  Indicates if this segment is related to another business entity.  This is only available if the Dynamic field equals Yes.  """  
      self.RefEntity:str = obj["RefEntity"]
      """  This is the reference entity where the COASegVals are generated from.  Valid values are found in the BusEntities table.  This option is NOT valid for the natural account (segment number 1)  """  
      self.AllowAlpha:bool = obj["AllowAlpha"]
      """  Indicates if alpha characters are allowed in the code.   The default value is yes.  If UseRefEntity equals yes then this field must equal yes.  If no, then only  numeric characters are allowed as segment values.  """  
      self.EntryControl:str = obj["EntryControl"]
      """   Indicates what causes the entry of segment values for this segment.  Valid values are: 0 (zero): Mandatory - the segment is always entered.  1 (one) Natrual account - The option on the natural account determines if this segment is mandatory, optional or not used.  This value is found on the COASegOpt table.
2 (two) - GL Reference Account Mask - only valid for segments defined as Use Ref Entity where the reference entity = 'Reference Entity'.
3 (three) - Optional.  The segment is not required to be entered.  """  
      self.SegSelfBal:bool = obj["SegSelfBal"]
      """  Indicates if journal entries are automatically balanced.  """  
      self.Level:int = obj["Level"]
      """  The level indicates the order segments will be balanced in case multiple segments are defined as self balancing.  This field can only be updated when SegSelfBal equals yes.  Two self balancing segments cannot have the same level.  Valid values are 1 thorugh the number of segments defined for the COA.  """  
      self.SummaryBal:bool = obj["SummaryBal"]
      """  Indicates if this segment is included in the summary balance GL Account.  Only those segments that are flagged as detail balance segments are eligible to be included as a summary balance segment.  """  
      self.DetailBal:bool = obj["DetailBal"]
      """  Indicates if balance records are maintained by the system for this segment.  If Yes, this segment is used as part of the GL Account for balance purposes.  """  
      self.KeepOpenBal:bool = obj["KeepOpenBal"]
      """  Indicates if opening balances are kept for expense and revenue accounts.  This is typically used for project accounting where you want to keep the project date balance independent of the financial year.  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  Indicates the order in which this segment is displayed when presenting the GL Account to the user.  Valid values are 1 through 20.  """  
      self.AutoCreateSegVals:bool = obj["AutoCreateSegVals"]
      """  Indicates if segment values for segments defined as reference entity are to be created each time a new record is created.  Only valid if UseRefEntity equals yes and a reference entity is entered.  """  
      self.SelfBalAcct:str = obj["SelfBalAcct"]
      """  Account used  when creating balancing transactions for this segment.  """  
      self.BalSegValue1:str = obj["BalSegValue1"]
      """  Balance Seg Value 1  """  
      self.BalSegValue2:str = obj["BalSegValue2"]
      """  Balance Seg Value 2  """  
      self.BalSegValue3:str = obj["BalSegValue3"]
      """  Balance Seg Value 3  """  
      self.BalSegValue4:str = obj["BalSegValue4"]
      """  Balance Seg Value 4  """  
      self.BalSegValue5:str = obj["BalSegValue5"]
      """  Balance Seg Value 5  """  
      self.BalSegValue6:str = obj["BalSegValue6"]
      """  Balance Seg Value 6  """  
      self.BalSegValue7:str = obj["BalSegValue7"]
      """  Balance Seg Value 7  """  
      self.BalSegValue8:str = obj["BalSegValue8"]
      """  Balance Seg Value 8  """  
      self.BalSegValue9:str = obj["BalSegValue9"]
      """  Balance Seg Value 9  """  
      self.BalSegValue10:str = obj["BalSegValue10"]
      """  Balance Seg Value 10  """  
      self.BalSegValue11:str = obj["BalSegValue11"]
      """  Balance Seg Value 11  """  
      self.BalSegValue12:str = obj["BalSegValue12"]
      """  Balance Seg Value 12  """  
      self.BalSegValue13:str = obj["BalSegValue13"]
      """  Balance Seg Value 13  """  
      self.BalSegValue14:str = obj["BalSegValue14"]
      """  Balance Seg Value 14  """  
      self.BalSegValue15:str = obj["BalSegValue15"]
      """  Balance Seg Value 15  """  
      self.BalSegValue16:str = obj["BalSegValue16"]
      """  Balance Seg Value 16  """  
      self.BalSegValue17:str = obj["BalSegValue17"]
      """  Balance Seg Value 17  """  
      self.BalSegValue18:str = obj["BalSegValue18"]
      """  Balance Seg Value 18  """  
      self.BalSegValue19:str = obj["BalSegValue19"]
      """  Balance Seg Value 19  """  
      self.BalSegValue20:str = obj["BalSegValue20"]
      """  Balance Seg Value 20  """  
      self.SelfOffAcct:str = obj["SelfOffAcct"]
      """  The Self Balance offset account used when balancing this segment.  """  
      self.OffSegValue1:str = obj["OffSegValue1"]
      """  Offset Segment Value 1  """  
      self.OffSegValue2:str = obj["OffSegValue2"]
      """  Offset Segment Value 2  """  
      self.OffSegValue3:str = obj["OffSegValue3"]
      """  Offset Segment Value 3  """  
      self.OffSegValue4:str = obj["OffSegValue4"]
      """  Offset Segment Value 4  """  
      self.OffSegValue5:str = obj["OffSegValue5"]
      """  Offset Segment Value 5  """  
      self.OffSegValue6:str = obj["OffSegValue6"]
      """  Offset Segment Value 6  """  
      self.OffSegValue7:str = obj["OffSegValue7"]
      """  Offset Segment Value 7  """  
      self.OffSegValue8:str = obj["OffSegValue8"]
      """  Offset Segment Value 8  """  
      self.OffSegValue9:str = obj["OffSegValue9"]
      """  Offset Segment Value 9  """  
      self.OffSegValue10:str = obj["OffSegValue10"]
      """  Offset Segment Value 10  """  
      self.OffSegValue11:str = obj["OffSegValue11"]
      """  Offset Segment Value 11  """  
      self.OffSegValue12:str = obj["OffSegValue12"]
      """  Offset Segment Value 12  """  
      self.OffSegValue13:str = obj["OffSegValue13"]
      """  Offset Segment Value 13  """  
      self.OffSegValue14:str = obj["OffSegValue14"]
      """  Offset Segment Value 14  """  
      self.OffSegValue15:str = obj["OffSegValue15"]
      """  Offset Segment Value 15  """  
      self.OffSegValue16:str = obj["OffSegValue16"]
      """  Offset Segment Value 16  """  
      self.OffSegValue17:str = obj["OffSegValue17"]
      """  Offset Segment Value 17  """  
      self.OffSegValue18:str = obj["OffSegValue18"]
      """  Offset Segment Value 18  """  
      self.OffSegValue19:str = obj["OffSegValue19"]
      """  Offset Segment Value 19  """  
      self.OffSegValue20:str = obj["OffSegValue20"]
      """  Offset Segment Value 20  """  
      self.ReverseCategoryID:str = obj["ReverseCategoryID"]
      """  Reverse Account Category.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CNIsCFICode:bool = obj["CNIsCFICode"]
      """  CNIsCFICode  """  
      self.SegValueField:str = obj["SegValueField"]
      """  The name of Business Entity field that represents segment value.  """  
      self.DescFieldName:str = obj["DescFieldName"]
      """  The name of Business Entity field that represents description of segment value.  """  
      self.GlobalCOASegment:bool = obj["GlobalCOASegment"]
      """  Marks the COASegment as Global  """  
      self.GlobalCOASegmentValues:bool = obj["GlobalCOASegmentValues"]
      """  Indicates COASegValues records for the COASegment will be used for Global  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates  """  
      self.GlobalValuesLock:bool = obj["GlobalValuesLock"]
      """  Disables Segment Values record from receiving global updates  """  
      self.SiteSegment:bool = obj["SiteSegment"]
      """  Indicates this is a Site Segment  """  
      self.BalancingAcctDesc:str = obj["BalancingAcctDesc"]
      """  Balancing Account Description  """  
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if a chart is in use  """  
      self.DisplayedLast:bool = obj["DisplayedLast"]
      """  Internal field not meant for end user use.  Logical used by row rules to disable the move up/down buttons on the display order tab.  """  
      self.OffsetAcctDesc:str = obj["OffsetAcctDesc"]
      """  Offset Account Description  """  
      self.SegmentInUse:bool = obj["SegmentInUse"]
      """  Logical indicates if a COAsegment has been used in a GL Account.  """  
      self.StructureFmtChg:bool = obj["StructureFmtChg"]
      """  Internal field not meant for end user use.  Logical indicating if a critical COA structure change has occurred.  """  
      self.UpdatedAuto:bool = obj["UpdatedAuto"]
      """  Dynamic Segment values using Business Entity will 'Updated Automatically'. Business Entity (DB table) should have additional code triggers. (e.g. Customer, Vendor)  """  
      self.AutoCreateSegValsInfo:str = obj["AutoCreateSegValsInfo"]
      self.EnableGlobalSeg:bool = obj["EnableGlobalSeg"]
      self.EnableGlobalSegLock:bool = obj["EnableGlobalSegLock"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.EnableGlobalSegValues:bool = obj["EnableGlobalSegValues"]
      self.EnableGlobalSegValuesLock:bool = obj["EnableGlobalSegValuesLock"]
      self.GlbValuesFlag:bool = obj["GlbValuesFlag"]
      self.SegValueFieldLength:int = obj["SegValueFieldLength"]
      """  Length of Business Entity field that represents segment value.  """  
      self.SiteIsLegalEntity:bool = obj["SiteIsLegalEntity"]
      """  Site is a Legal Entity  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BusEntityDescDescription:str = obj["BusEntityDescDescription"]
      self.BusEntityDescEntityType:str = obj["BusEntityDescEntityType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COATableset:
   def __init__(self, obj):
      self.COA:list[Erp_Tablesets_COARow] = obj["COA"]
      self.COASegment:list[Erp_Tablesets_COASegmentRow] = obj["COASegment"]
      self.COASegmentNotCreated:list[Erp_Tablesets_COASegmentNotCreatedRow] = obj["COASegmentNotCreated"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCOATableset:
   def __init__(self, obj):
      self.COA:list[Erp_Tablesets_COARow] = obj["COA"]
      self.COASegment:list[Erp_Tablesets_COASegmentRow] = obj["COASegment"]
      self.COASegmentNotCreated:list[Erp_Tablesets_COASegmentNotCreatedRow] = obj["COASegmentNotCreated"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByIDOrdered_input:
   """ Required : 
   COACode
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      pass

class GetByIDOrdered_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COATableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   coACode
   """  
   def __init__(self, obj):
      self.coACode:str = obj["coACode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COATableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COATableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COATableset] = obj["returnObj"]
      pass

class GetCOAGlobalFields_input:
   """ Required : 
   COACode
   GlobalLock
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      self.GlobalLock:bool = obj["GlobalLock"]
      pass

class GetCOAGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCOASegmentGlobalFields_input:
   """ Required : 
   COACode
   SegmentNbr
   GlobalLock
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      self.SegmentNbr:int = obj["SegmentNbr"]
      self.GlobalLock:bool = obj["GlobalLock"]
      pass

class GetCOASegmentGlobalFields_output:
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
      self.returnObj:list[Erp_Tablesets_COAListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMaxLength_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class GetMaxLength_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetNewCOASegment_input:
   """ Required : 
   ds
   coACode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      pass

class GetNewCOASegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCOA_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class GetNewCOA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCOA
   whereClauseCOASegment
   whereClauseCOASegmentNotCreated
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCOA:str = obj["whereClauseCOA"]
      self.whereClauseCOASegment:str = obj["whereClauseCOASegment"]
      self.whereClauseCOASegmentNotCreated:str = obj["whereClauseCOASegmentNotCreated"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COATableset] = obj["returnObj"]
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

class IsCOAMasterCOA_input:
   """ Required : 
   ipCOACode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      pass

class IsCOAMasterCOA_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class IsChartInUse_input:
   """ Required : 
   ipCOACode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      pass

class IsChartInUse_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class IsChartUsedInTransaction_input:
   """ Required : 
   ipCOACode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      pass

class IsChartUsedInTransaction_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class IsSegValInUse_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   ipSegmentVal
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment Number  """  
      self.ipSegmentVal:str = obj["ipSegmentVal"]
      """  Segement Code/Value  """  
      pass

class IsSegValInUse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opValInUse:bool = obj["opValInUse"]
      pass

      """  output parameters  """  

class MoveOnePositionReturnNewIndex_input:
   """ Required : 
   COACode
   segmentNbr
   displayOrder
   moveDir
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.displayOrder:int = obj["displayOrder"]
      self.moveDir:str = obj["moveDir"]
      pass

class MoveOnePositionReturnNewIndex_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COATableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.newRowPosition:int = obj["parameters"]
      pass

      """  output parameters  """  

class MoveOnePosition_input:
   """ Required : 
   coaCode
   segmentNbr
   dynamicOpt
   displayOrder
   moveDir
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  Chart of Accounts Code  """  
      self.segmentNbr:int = obj["segmentNbr"]
      """  COA Segment Number  """  
      self.dynamicOpt:bool = obj["dynamicOpt"]
      """  Indicates if a dynamic (yes) or controlled (no) segment (yes) is being moved  """  
      self.displayOrder:int = obj["displayOrder"]
      """  Current display order  """  
      self.moveDir:str = obj["moveDir"]
      """  Direction to move task, "Up" or "Down"  """  
      pass

class MoveOnePosition_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COATableset] = obj["returnObj"]
      pass

class PromptAutoCreateDynSegVals_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class PromptAutoCreateDynSegVals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      self.opAutoCreateSegValMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetRefEntityFields_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class SetRefEntityFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateCOADynamicSegValues_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment Number  """  
      pass

class UpdateCOADynamicSegValues_output:
   def __init__(self, obj):
      pass

class UpdateDynamicSegment_input:
   """ Required : 
   ipDynamic
   ds
   """  
   def __init__(self, obj):
      self.ipDynamic:bool = obj["ipDynamic"]
      """  Proposed value of COASegment.Dynamic  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class UpdateDynamicSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOATableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOATableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateFieldLength_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class UpdateFieldLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateMaxLength_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class UpdateMaxLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateNatural_input:
   """ Required : 
   ipGlobal
   ds
   """  
   def __init__(self, obj):
      self.ipGlobal:bool = obj["ipGlobal"]
      """  Proposed value of COA.Global  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class UpdateNatural_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateEntryControl_input:
   """ Required : 
   ipSegmentNbr
   ipRefEntity
   ipEntryControl
   """  
   def __init__(self, obj):
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment Number  """  
      self.ipRefEntity:str = obj["ipRefEntity"]
      """  Reference entity value  """  
      self.ipEntryControl:str = obj["ipEntryControl"]
      """  Entry Control  """  
      pass

class ValidateEntryControl_output:
   def __init__(self, obj):
      pass

class ValidateRefEntity_input:
   """ Required : 
   ipRefEntity
   ds
   """  
   def __init__(self, obj):
      self.ipRefEntity:str = obj["ipRefEntity"]
      """  Reference Entity to validate  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class ValidateRefEntity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      self.opAutoCreateSegValMsg:str = obj["parameters"]
      self.opValuesAlreadyExist:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateSegmentMaxLength_input:
   """ Required : 
   ipMaxLength
   ds
   """  
   def __init__(self, obj):
      self.ipMaxLength:int = obj["ipMaxLength"]
      """  Proposed value of COASegment.MaxLength  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class ValidateSegmentMaxLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSegmentMinLength_input:
   """ Required : 
   ipMinLength
   ds
   """  
   def __init__(self, obj):
      self.ipMinLength:int = obj["ipMinLength"]
      """  Proposed value of COASegment.MaxLength  """  
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

class ValidateSegmentMinLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COATableset] = obj["ds"]
      pass

      """  output parameters  """  

class WarnNewMandatorySegmentDynamicExt_input:
   """ Required : 
   coaCode
   segNbr
   entryControl
   dynamic
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA Code  """  
      self.segNbr:int = obj["segNbr"]
      """  Segment Number  """  
      self.entryControl:str = obj["entryControl"]
      """  Entry Control  """  
      self.dynamic:bool = obj["dynamic"]
      """  Dynamic Segment flag  """  
      pass

class WarnNewMandatorySegmentDynamicExt_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Returns warning if new mandatory segment has been added for the COA in use. Message depends on whether new segment is dynamic.  """  
      pass

class WarnNewMandatorySegmentDynamic_input:
   """ Required : 
   coaCode
   entryControl
   dynamic
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA Code  """  
      self.entryControl:str = obj["entryControl"]
      """  Entry Control  """  
      self.dynamic:bool = obj["dynamic"]
      """  Dynamic Segment flag  """  
      pass

class WarnNewMandatorySegmentDynamic_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Returns warning if new mandatory segment has been added for the COA in use. Message depends on whether new segment is dynamic.  """  
      pass

