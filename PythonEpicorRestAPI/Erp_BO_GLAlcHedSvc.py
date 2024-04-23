import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLAlcHedSvc
# Description: G/L Account Allocation - BL
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcHeds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLAlcHeds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAlcHeds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAlcHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHeds",headers=creds) as resp:
           return await resp.json()

async def post_GLAlcHeds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAlcHeds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAlcHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLAlcHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHeds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLAlcHeds_Company_AllocID(Company, AllocID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAlcHed item
   Description: Calls GetByID to retrieve the GLAlcHed item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAlcHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAlcHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHeds(" + Company + "," + AllocID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLAlcHeds_Company_AllocID(Company, AllocID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLAlcHed for the service
   Description: Calls UpdateExt to update GLAlcHed. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAlcHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAlcHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHeds(" + Company + "," + AllocID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLAlcHeds_Company_AllocID(Company, AllocID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLAlcHed item
   Description: Call UpdateExt to delete GLAlcHed item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAlcHed
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHeds(" + Company + "," + AllocID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcHeds_Company_AllocID_GLAlcDtls(Company, AllocID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLAlcDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLAlcDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAlcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHeds(" + Company + "," + AllocID + ")/GLAlcDtls",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcHeds_Company_AllocID_GLAlcDtls_Company_AllocID_AllocLine(Company, AllocID, AllocLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAlcDtl item
   Description: Calls GetByID to retrieve the GLAlcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAlcDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocLine: Desc: AllocLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAlcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHeds(" + Company + "," + AllocID + ")/GLAlcDtls(" + Company + "," + AllocID + "," + AllocLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcHeds_Company_AllocID_GLAlcHedTGLCs(Company, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLAlcHedTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLAlcHedTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAlcHedTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHeds(" + Company + "," + AllocID + ")/GLAlcHedTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcHeds_Company_AllocID_GLAlcHedTGLCs_Company_AllocID_TGLCTranNum(Company, AllocID, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAlcHedTGLC item
   Description: Calls GetByID to retrieve the GLAlcHedTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAlcHedTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAlcHedTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHeds(" + Company + "," + AllocID + ")/GLAlcHedTGLCs(" + Company + "," + AllocID + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLAlcDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAlcDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAlcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtls",headers=creds) as resp:
           return await resp.json()

async def post_GLAlcDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAlcDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAlcDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLAlcDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLAlcDtls_Company_AllocID_AllocLine(Company, AllocID, AllocLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAlcDtl item
   Description: Calls GetByID to retrieve the GLAlcDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAlcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocLine: Desc: AllocLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAlcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtls(" + Company + "," + AllocID + "," + AllocLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLAlcDtls_Company_AllocID_AllocLine(Company, AllocID, AllocLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLAlcDtl for the service
   Description: Calls UpdateExt to update GLAlcDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAlcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocLine: Desc: AllocLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAlcDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtls(" + Company + "," + AllocID + "," + AllocLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLAlcDtls_Company_AllocID_AllocLine(Company, AllocID, AllocLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLAlcDtl item
   Description: Call UpdateExt to delete GLAlcDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAlcDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocLine: Desc: AllocLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtls(" + Company + "," + AllocID + "," + AllocLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcDtls_Company_AllocID_AllocLine_GLAlcDtlTGLCs(Company, AllocID, AllocLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLAlcDtlTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLAlcDtlTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocLine: Desc: AllocLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAlcDtlTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtls(" + Company + "," + AllocID + "," + AllocLine + ")/GLAlcDtlTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcDtls_Company_AllocID_AllocLine_GLAlcDtlTGLCs_Company_AllocID_AllocLine_TGLCTranNum(Company, AllocID, AllocLine, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAlcDtlTGLC item
   Description: Calls GetByID to retrieve the GLAlcDtlTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAlcDtlTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocLine: Desc: AllocLine   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAlcDtlTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtls(" + Company + "," + AllocID + "," + AllocLine + ")/GLAlcDtlTGLCs(" + Company + "," + AllocID + "," + AllocLine + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcDtlTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLAlcDtlTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAlcDtlTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAlcDtlTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtlTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_GLAlcDtlTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAlcDtlTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAlcDtlTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLAlcDtlTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtlTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLAlcDtlTGLCs_Company_AllocID_AllocLine_TGLCTranNum(Company, AllocID, AllocLine, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAlcDtlTGLC item
   Description: Calls GetByID to retrieve the GLAlcDtlTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAlcDtlTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocLine: Desc: AllocLine   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAlcDtlTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtlTGLCs(" + Company + "," + AllocID + "," + AllocLine + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLAlcDtlTGLCs_Company_AllocID_AllocLine_TGLCTranNum(Company, AllocID, AllocLine, TGLCTranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLAlcDtlTGLC for the service
   Description: Calls UpdateExt to update GLAlcDtlTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAlcDtlTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocLine: Desc: AllocLine   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAlcDtlTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtlTGLCs(" + Company + "," + AllocID + "," + AllocLine + "," + TGLCTranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLAlcDtlTGLCs_Company_AllocID_AllocLine_TGLCTranNum(Company, AllocID, AllocLine, TGLCTranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLAlcDtlTGLC item
   Description: Call UpdateExt to delete GLAlcDtlTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAlcDtlTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocLine: Desc: AllocLine   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcDtlTGLCs(" + Company + "," + AllocID + "," + AllocLine + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLAlcHedTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLAlcHedTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAlcHedTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAlcHedTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHedTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_GLAlcHedTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAlcHedTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAlcHedTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLAlcHedTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHedTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLAlcHedTGLCs_Company_AllocID_TGLCTranNum(Company, AllocID, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAlcHedTGLC item
   Description: Calls GetByID to retrieve the GLAlcHedTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAlcHedTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAlcHedTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHedTGLCs(" + Company + "," + AllocID + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLAlcHedTGLCs_Company_AllocID_TGLCTranNum(Company, AllocID, TGLCTranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLAlcHedTGLC for the service
   Description: Calls UpdateExt to update GLAlcHedTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAlcHedTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAlcHedTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHedTGLCs(" + Company + "," + AllocID + "," + TGLCTranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLAlcHedTGLCs_Company_AllocID_TGLCTranNum(Company, AllocID, TGLCTranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLAlcHedTGLC item
   Description: Call UpdateExt to delete GLAlcHedTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAlcHedTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/GLAlcHedTGLCs(" + Company + "," + AllocID + "," + TGLCTranNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAlcHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLAlcHed, whereClauseGLAlcDtl, whereClauseGLAlcDtlTGLC, whereClauseGLAlcHedTGLC, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseGLAlcHed=" + whereClauseGLAlcHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLAlcDtl=" + whereClauseGLAlcDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLAlcDtlTGLC=" + whereClauseGLAlcDtlTGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLAlcHedTGLC=" + whereClauseGLAlcHedTGLC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(allocID, epicorHeaders = None):
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
   params += "allocID=" + allocID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPercent
   OperationID: GetPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLAlcHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLAlcHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAlcHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLAlcHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAlcHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLAlcDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLAlcDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAlcDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLAlcDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAlcDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLAlcDtlTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLAlcDtlTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAlcDtlTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLAlcDtlTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAlcDtlTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLAlcHedTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLAlcHedTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAlcHedTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLAlcHedTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAlcHedTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLAlcHedSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAlcDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAlcDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAlcDtlTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAlcDtlTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAlcHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAlcHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAlcHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAlcHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAlcHedTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAlcHedTGLCRow] = obj["value"]
      pass

class Erp_Tablesets_GLAlcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  The allocation ID value (GLAlcHed.AllocID) of the allocation that this record is related to.  """  
      self.AllocLine:int = obj["AllocLine"]
      """  An internally assigned integer which is used as part of the key to uniquely identify the record.  """  
      self.AllocationUnits:int = obj["AllocationUnits"]
      """   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount to the GL account number. Total Allocation units are calculated for a given AllocID and not stored.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Percent:int = obj["Percent"]
      self.TotalAllocationUnits:int = obj["TotalAllocationUnits"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.BitFlag:int = obj["BitFlag"]
      self.AllocIDDescription:str = obj["AllocIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAlcDtlTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.AllocLine:int = obj["AllocLine"]
      """  AllocLine of GLAlcDtl  """  
      self.AllocID:str = obj["AllocID"]
      """  AllocID of GLAlcDtl  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAlcHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Unique identifier of the allocation assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description of the allocation.  """  
      self.Basis:str = obj["Basis"]
      """  What the allocation units are based on.  For reference purposes only.  Ex: Sq. Feet, Percentage, ...etc.  """  
      self.LastDate:str = obj["LastDate"]
      """  Last date on which a journal entry was created with this allocation.  """  
      self.LastUser:str = obj["LastUser"]
      """  User ID that last created a journal entry with this allocation.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAlcHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Unique identifier of the allocation assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description of the allocation.  """  
      self.Basis:str = obj["Basis"]
      """  What the allocation units are based on.  For reference purposes only.  Ex: Sq. Feet, Percentage, ...etc.  """  
      self.LastDate:str = obj["LastDate"]
      """  Last date on which a journal entry was created with this allocation.  """  
      self.LastUser:str = obj["LastUser"]
      """  User ID that last created a journal entry with this allocation.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GLAcct:str = obj["GLAcct"]
      """  G/L Display Account  """  
      self.TotalAllocationUnits:int = obj["TotalAllocationUnits"]
      """  Total Allocation Units  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.BookID:str = obj["BookID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAlcHedTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.AllocID:str = obj["AllocID"]
      """  AllocID of GLAlcHed  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   allocID
   """  
   def __init__(self, obj):
      self.allocID:str = obj["allocID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLAlcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  The allocation ID value (GLAlcHed.AllocID) of the allocation that this record is related to.  """  
      self.AllocLine:int = obj["AllocLine"]
      """  An internally assigned integer which is used as part of the key to uniquely identify the record.  """  
      self.AllocationUnits:int = obj["AllocationUnits"]
      """   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount to the GL account number. Total Allocation units are calculated for a given AllocID and not stored.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Percent:int = obj["Percent"]
      self.TotalAllocationUnits:int = obj["TotalAllocationUnits"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.BitFlag:int = obj["BitFlag"]
      self.AllocIDDescription:str = obj["AllocIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAlcDtlTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.AllocLine:int = obj["AllocLine"]
      """  AllocLine of GLAlcDtl  """  
      self.AllocID:str = obj["AllocID"]
      """  AllocID of GLAlcDtl  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAlcHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Unique identifier of the allocation assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description of the allocation.  """  
      self.Basis:str = obj["Basis"]
      """  What the allocation units are based on.  For reference purposes only.  Ex: Sq. Feet, Percentage, ...etc.  """  
      self.LastDate:str = obj["LastDate"]
      """  Last date on which a journal entry was created with this allocation.  """  
      self.LastUser:str = obj["LastUser"]
      """  User ID that last created a journal entry with this allocation.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAlcHedListTableset:
   def __init__(self, obj):
      self.GLAlcHedList:list[Erp_Tablesets_GLAlcHedListRow] = obj["GLAlcHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLAlcHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AllocID:str = obj["AllocID"]
      """  Unique identifier of the allocation assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description of the allocation.  """  
      self.Basis:str = obj["Basis"]
      """  What the allocation units are based on.  For reference purposes only.  Ex: Sq. Feet, Percentage, ...etc.  """  
      self.LastDate:str = obj["LastDate"]
      """  Last date on which a journal entry was created with this allocation.  """  
      self.LastUser:str = obj["LastUser"]
      """  User ID that last created a journal entry with this allocation.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GLAcct:str = obj["GLAcct"]
      """  G/L Display Account  """  
      self.TotalAllocationUnits:int = obj["TotalAllocationUnits"]
      """  Total Allocation Units  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.BookID:str = obj["BookID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAlcHedTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.AllocID:str = obj["AllocID"]
      """  AllocID of GLAlcHed  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAlcHedTableset:
   def __init__(self, obj):
      self.GLAlcHed:list[Erp_Tablesets_GLAlcHedRow] = obj["GLAlcHed"]
      self.GLAlcDtl:list[Erp_Tablesets_GLAlcDtlRow] = obj["GLAlcDtl"]
      self.GLAlcDtlTGLC:list[Erp_Tablesets_GLAlcDtlTGLCRow] = obj["GLAlcDtlTGLC"]
      self.GLAlcHedTGLC:list[Erp_Tablesets_GLAlcHedTGLCRow] = obj["GLAlcHedTGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLAlcHedTableset:
   def __init__(self, obj):
      self.GLAlcHed:list[Erp_Tablesets_GLAlcHedRow] = obj["GLAlcHed"]
      self.GLAlcDtl:list[Erp_Tablesets_GLAlcDtlRow] = obj["GLAlcDtl"]
      self.GLAlcDtlTGLC:list[Erp_Tablesets_GLAlcDtlTGLCRow] = obj["GLAlcDtlTGLC"]
      self.GLAlcHedTGLC:list[Erp_Tablesets_GLAlcHedTGLCRow] = obj["GLAlcHedTGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   allocID
   """  
   def __init__(self, obj):
      self.allocID:str = obj["allocID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAlcHedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAlcHedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAlcHedTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLAlcHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLAlcDtlTGLC_input:
   """ Required : 
   ds
   allocID
   allocLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      self.allocLine:int = obj["allocLine"]
      pass

class GetNewGLAlcDtlTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLAlcDtl_input:
   """ Required : 
   ds
   allocID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      pass

class GetNewGLAlcDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLAlcHedTGLC_input:
   """ Required : 
   ds
   allocID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      self.allocID:str = obj["allocID"]
      pass

class GetNewGLAlcHedTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLAlcHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      pass

class GetNewGLAlcHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPercent_input:
   """ Required : 
   AllocationUnits
   TotalAllocationUnits
   """  
   def __init__(self, obj):
      self.AllocationUnits:int = obj["AllocationUnits"]
      self.TotalAllocationUnits:int = obj["TotalAllocationUnits"]
      pass

class GetPercent_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseGLAlcHed
   whereClauseGLAlcDtl
   whereClauseGLAlcDtlTGLC
   whereClauseGLAlcHedTGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLAlcHed:str = obj["whereClauseGLAlcHed"]
      self.whereClauseGLAlcDtl:str = obj["whereClauseGLAlcDtl"]
      self.whereClauseGLAlcDtlTGLC:str = obj["whereClauseGLAlcDtlTGLC"]
      self.whereClauseGLAlcHedTGLC:str = obj["whereClauseGLAlcHedTGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLAlcHedTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtGLAlcHedTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLAlcHedTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAlcHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

