import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.COAPESvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_COAPEs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COAPEs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COAPEs
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COAPEs",headers=creds) as resp:
           return await resp.json()

async def post_COAPEs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COAPEs
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COAPEs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COAPEs_Company_COACode(Company, COACode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COAPE item
   Description: Calls GetByID to retrieve the COAPE item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COAPE
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COAPEs(" + Company + "," + COACode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COAPEs_Company_COACode(Company, COACode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COAPE for the service
   Description: Calls UpdateExt to update COAPE. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COAPE
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COAPEs(" + Company + "," + COACode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COAPEs_Company_COACode(Company, COACode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COAPE item
   Description: Call UpdateExt to delete COAPE item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COAPE
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COAPEs(" + Company + "," + COACode + ")",headers=creds) as resp:
           return await resp.json()

async def get_COAPEs_Company_COACode_COASegments(Company, COACode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get COASegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COAPEs(" + Company + "," + COACode + ")/COASegments",headers=creds) as resp:
           return await resp.json()

async def get_COAPEs_Company_COACode_COASegments_Company_COACode_SegmentNbr(Company, COACode, SegmentNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegment item
   Description: Calls GetByID to retrieve the COASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COAPEs(" + Company + "," + COACode + ")/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegments(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COASegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegments
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegments",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COASegments_Company_COACode_SegmentNbr(Company, COACode, SegmentNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegment item
   Description: Calls GetByID to retrieve the COASegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegments_Company_COACode_SegmentNbr_COASegValues(Company, COACode, SegmentNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get COASegValues items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COASegValues1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")/COASegValues",headers=creds) as resp:
           return await resp.json()

async def get_COASegments_Company_COACode_SegmentNbr_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company, COACode, SegmentNbr, SegmentCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegValue item
   Description: Calls GetByID to retrieve the COASegValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegValue1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegments(" + Company + "," + COACode + "," + SegmentNbr + ")/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_COASegValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COASegValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COASegValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegValues",headers=creds) as resp:
           return await resp.json()

async def post_COASegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company, COACode, SegmentNbr, SegmentCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COASegValue item
   Description: Calls GetByID to retrieve the COASegValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company, COACode, SegmentNbr, SegmentCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COASegValue for the service
   Description: Calls UpdateExt to update COASegValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COASegValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COASegValues_Company_COACode_SegmentNbr_SegmentCode(Company, COACode, SegmentNbr, SegmentCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COASegValue item
   Description: Call UpdateExt to delete COASegValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/COASegValues(" + Company + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCOA, whereClauseCOASegment, whereClauseCOASegValues, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCOASegValues=" + whereClauseCOASegValues
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOASegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOASegValues
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOASegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOASegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAPESvc/List", json=requestBody,headers=creds) as resp:
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

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COASegValuesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COASegValuesRow] = obj["value"]
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

class Erp_Tablesets_COASegValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Curency Account  """  
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      """   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  StatUOMCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  Identifies the account category this is used to determine characteristics when the segment value is reversed.  """  
      self.ExtAnalysisCode:str = obj["ExtAnalysisCode"]
      """  External financial analysis code linked to the natural account.  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.BENAEID:str = obj["BENAEID"]
      """  Non-Admissible Expense Code (CSF Belgium)  """  
      self.Mapped:bool = obj["Mapped"]
      """  Mapped  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text.  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.LinkedPlant:str = obj["LinkedPlant"]
      """  LinkedPlant  """  
      self.AccrualAcctDesc:str = obj["AccrualAcctDesc"]
      """  Accrual Account Description  """  
      self.GainAcctDesc:str = obj["GainAcctDesc"]
      """  Gain Account Description  """  
      self.GlbValuesFlag:bool = obj["GlbValuesFlag"]
      self.GlobalSegValues:bool = obj["GlobalSegValues"]
      self.GlobalSegValuesLock:bool = obj["GlobalSegValuesLock"]
      self.LossAcctDesc:str = obj["LossAcctDesc"]
      """  Loss Account Description  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.RefTypeRqd:bool = obj["RefTypeRqd"]
      """  Logical indicating if the reference type is required for this segment value  """  
      self.ReverseCategoryDescription:str = obj["ReverseCategoryDescription"]
      self.SegNbrName:str = obj["SegNbrName"]
      """  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  """  
      self.SegValInUse:bool = obj["SegValInUse"]
      """  Logical indicating if this segment value has been used.  """  
      self.SegWithSegOneControl:bool = obj["SegWithSegOneControl"]
      """  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if this chart has been used.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CategoryIDDescription:str = obj["CategoryIDDescription"]
      self.COASegmentSiteSegment:bool = obj["COASegmentSiteSegment"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.COSegDtlSegmentName:str = obj["COSegDtlSegmentName"]
      self.CreditRateGrpDescription:str = obj["CreditRateGrpDescription"]
      self.DebitRateGrpDescription:str = obj["DebitRateGrpDescription"]
      self.GLCOARefTypeRefTypeDesc:str = obj["GLCOARefTypeRefTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.BudgetSegCode_c:str = obj["BudgetSegCode_c"]
      self.BudgetReportGroup_c:str = obj["BudgetReportGroup_c"]
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

class Erp_Tablesets_COAPETableset:
   def __init__(self, obj):
      self.COA:list[Erp_Tablesets_COARow] = obj["COA"]
      self.COASegment:list[Erp_Tablesets_COASegmentRow] = obj["COASegment"]
      self.COASegValues:list[Erp_Tablesets_COASegValuesRow] = obj["COASegValues"]
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

class Erp_Tablesets_COASegValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      """  Curency Account  """  
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the COASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      """   0)      Summarize (default)
1)      Summarize debit and credits separately
2)      No summarization  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  StatUOMCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  Identifies the account category this is used to determine characteristics when the segment value is reversed.  """  
      self.ExtAnalysisCode:str = obj["ExtAnalysisCode"]
      """  External financial analysis code linked to the natural account.  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.BENAEID:str = obj["BENAEID"]
      """  Non-Admissible Expense Code (CSF Belgium)  """  
      self.Mapped:bool = obj["Mapped"]
      """  Mapped  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text.  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.LinkedPlant:str = obj["LinkedPlant"]
      """  LinkedPlant  """  
      self.AccrualAcctDesc:str = obj["AccrualAcctDesc"]
      """  Accrual Account Description  """  
      self.GainAcctDesc:str = obj["GainAcctDesc"]
      """  Gain Account Description  """  
      self.GlbValuesFlag:bool = obj["GlbValuesFlag"]
      self.GlobalSegValues:bool = obj["GlobalSegValues"]
      self.GlobalSegValuesLock:bool = obj["GlobalSegValuesLock"]
      self.LossAcctDesc:str = obj["LossAcctDesc"]
      """  Loss Account Description  """  
      self.RebuildGLAccts:bool = obj["RebuildGLAccts"]
      """  Internal logical used by UI that indicates if GLAccounts exist for this COA and that the display gl account must be rebuilt  """  
      self.RefTypeRqd:bool = obj["RefTypeRqd"]
      """  Logical indicating if the reference type is required for this segment value  """  
      self.ReverseCategoryDescription:str = obj["ReverseCategoryDescription"]
      self.SegNbrName:str = obj["SegNbrName"]
      """  Segment number name from the COASegment table.  Used for display purposes in segment value searches where more than one segment number is searched at a time.  """  
      self.SegValInUse:bool = obj["SegValInUse"]
      """  Logical indicating if this segment value has been used.  """  
      self.SegWithSegOneControl:bool = obj["SegWithSegOneControl"]
      """  Logical indicating whether or not the COA has a segment defined as 'entry control' equal to natural account and controls whether or not a segment option record can be entered for a natural account value.  """  
      self.StatisticalDesc:str = obj["StatisticalDesc"]
      self.ChartInUse:bool = obj["ChartInUse"]
      """  Logical indicating if this chart has been used.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CategoryIDDescription:str = obj["CategoryIDDescription"]
      self.COASegmentSiteSegment:bool = obj["COASegmentSiteSegment"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.COSegDtlSegmentName:str = obj["COSegDtlSegmentName"]
      self.CreditRateGrpDescription:str = obj["CreditRateGrpDescription"]
      self.DebitRateGrpDescription:str = obj["DebitRateGrpDescription"]
      self.GLCOARefTypeRefTypeDesc:str = obj["GLCOARefTypeRefTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.BudgetSegCode_c:str = obj["BudgetSegCode_c"]
      self.BudgetReportGroup_c:str = obj["BudgetReportGroup_c"]
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

class Erp_Tablesets_UpdExtCOAPETableset:
   def __init__(self, obj):
      self.COA:list[Erp_Tablesets_COARow] = obj["COA"]
      self.COASegment:list[Erp_Tablesets_COASegmentRow] = obj["COASegment"]
      self.COASegValues:list[Erp_Tablesets_COASegValuesRow] = obj["COASegValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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
      self.returnObj:list[Erp_Tablesets_COAPETableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COAPETableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COAPETableset] = obj["returnObj"]
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

class GetNewCOASegValues_input:
   """ Required : 
   ds
   coACode
   segmentNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAPETableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      pass

class GetNewCOASegValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAPETableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCOASegment_input:
   """ Required : 
   ds
   coACode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAPETableset] = obj["ds"]
      self.coACode:str = obj["coACode"]
      pass

class GetNewCOASegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAPETableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCOA_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAPETableset] = obj["ds"]
      pass

class GetNewCOA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAPETableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCOA
   whereClauseCOASegment
   whereClauseCOASegValues
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCOA:str = obj["whereClauseCOA"]
      self.whereClauseCOASegment:str = obj["whereClauseCOASegment"]
      self.whereClauseCOASegValues:str = obj["whereClauseCOASegValues"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COAPETableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCOAPETableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOAPETableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAPETableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAPETableset] = obj["ds"]
      pass

      """  output parameters  """  

